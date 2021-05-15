import json 
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Game, BlackChessBoard, WhiteChessBoard
from accounts.models import User
from django.shortcuts import get_object_or_404
from enum import Enum 

class pawns(Enum):
    PAWN = 'pawn'
    KNIGHT = 'knight'
    QUEEN = 'queen'
    BISHOP = 'bishop'
    ROOK = 'rook'
    KING = 'king'

class color(Enum):
    BLACK = 'black'
    WHITE = 'white'
    

class GameConsumer(WebsocketConsumer):

    def get_chess_pos(self, data):
        game = get_object_or_404(Game, id=data['gameId'])
        content = {
            'command': 'positions',
            'white_pos': Game.get_white_pos(game),
            'black_pos': Game.get_black_pos(game)
        }
        self.send_to_frontend(content)

    def complete_game(self, data):
        game = get_object_or_404(Game, id=data['gameId'])
        game.winner = data['winner']
        game.completed = True
        game.save()

    def move_pawn(self, data):
        game = get_object_or_404(Game, id=data['gameId'])
        if game.who_has_turn == self.user:
            if data['color'] == color.WHITE:
                board = WhiteChessBoard.objects.get(id=game.WhiteChessBoard)
            elif data['color'] == color.BLACK:
                board = BlackChessBoard.objects.get(id=game.BlackChessBoard)

            if data['pawn'] == pawns.PAWN:
                board.pawns[data['id_pawn']] = data['new_field']
                board.save()
            elif data['pawn'] == pawns.KNIGHT:
                board.knights = data['new_field']
                board.save()
            elif data['pawn'] == pawns.QUEEN:
                board.queen = data['new_field']
                board.save()
            elif data['pawn'] == pawns.BISHOP:
                board.bishops[data['id_pawn']] = data['new_field']
                board.save()
            elif data['pawn'] == pawns.ROOK:
                board.rooks[data['id_pawn']] = data['new_field']
                board.save()
            elif data['pawn'] == pawns.KING:
                board.king[data['id_pawn']] = data['new_field']
                board.save()

            Game.next_turn(game)

        content = {
            'command': 'positions',
            'white_pos': Game.get_white_pos(game),
            'black_pos': Game.get_black_pos(game)
        }
        self.send_to_game(content)
        
    
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'game_{self.room_name}' 
         
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

    def send_to_game(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'game',
                'message': message
            }
        )

    def game(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))

    commands = {
        'get_chess_pos': get_chess_pos,
        'move_pawn': move_pawn,
        'complete_game': complete_game
    }
