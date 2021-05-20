from django.db import models 
from accounts.models import User 
from django.contrib.postgres.fields import ArrayField
from datetime import datetime


class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_message', null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    @staticmethod    
    def message_to_json(message):
        result = {
            'id': message.id,
            'author': message.author.username,
            'content': message.content,
            'date': str(message.date)[10:16]
        }
        return result

class Chat(models.Model):
    members = models.ManyToManyField(User, related_name='memebers', blank=True) 
    messages = models.ManyToManyField(Message, blank=True)
   

    @staticmethod
    def get_last_messasges(chat):
        messages = chat.messages.order_by('-date').all()[:10]
        json_messages = [{'id': message.id,
                          'author': message.author.username,
                          'content': message.content,
                          'date': str(message.date)[10:16]} for message in messages]
        return json_messages
     
    
