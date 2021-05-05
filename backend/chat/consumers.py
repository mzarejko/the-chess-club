import json 
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message, Chat
from accounts.models import User
from django.shortcuts import get_object_or_404


# synchronous consumer - less possibility of conflicts
class ChatConsumer(WebsocketConsumer):


    def fetch_messages(self, data):
        chat = get_object_or_404(Chat, id=data['chatId'])
        messages = Chat.get_last_messasges(chat)
        content = {
            'command': 'messages',
            'messages': messages
        }
        self.send_to_frontend(content)    

    def new_message(self, data):
        message = Message.objects.create(author=self.user,
                                         content=data['message'])
        chat = get_object_or_404(Chat, id = data['chatId'])
        chat.messages.add(message)
        content = {
            'command': 'new_message',
            'message': Message.message_to_json(message) 
        }
        return self.send_to_chat(content)

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}' 
         
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.user = self.scope["user"]
        # accept hendshake
        self.accept()


    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)
    
    
    def send_to_frontend(self, message):
        self.send(text_data=json.dumps(message))

    def send_to_chat(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat',
                'message': message
            }
        )

    def chat(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))


    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message 
    }
