import json 
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Game, BlackChessBoard, WhiteChessBoard
from accounts.models import User
from django.shortcuts import get_object_or_404
from enum import Enum, auto

class Chess(Enum):
    PAWN = 1
    KNIGHT = 2
    QUEEN = 3
    BISHOP = 4
    ROOK = 5
    KING = 6

class Color(Enum):
    BLACK = 1
    WHITE = 2

class Commands(str, Enum):
    FETCH_POSITONS = 'fetch_positions'
    MOVE_CHESS_PIECE = 'move_piece'

    

class GameConsumer(WebsocketConsumer):

    def fetch_positions(self, data):
        game = get_object_or_404(Game, id=data['gameId'])
        content = {
            'command': 'positions',
            'white_pos': Game.get_white_pos(game),
            'black_pos': Game.get_black_pos(game)
        }
        self.send_to_frontend(content)


    def move_piece(self, data):
        game = get_object_or_404(Game, id=data['gameId'])
        if game.who_has_turn == self.user:
            if data['color'] == Color.WHITE:
                board = WhiteChessBoard.objects.get(id=game.WhiteChessBoard)
            elif data['color'] == Color.BLACK:
                board = BlackChessBoard.objects.get(id=game.BlackChessBoard)

            if data['pawn'] == Chess.PAWN:
                board.pawns[data['id_pawn']] = data['new_field']
                board.save()
            elif data['pawn'] == Chess.KNIGHT:
                board.knights = data['new_field']
                board.save()
            elif data['pawn'] == Chess.QUEEN:
                board.queen = data['new_field']
                board.save()
            elif data['pawn'] == Chess.BISHOP:
                board.bishops[data['id_pawn']] = data['new_field']
                board.save()
            elif data['pawn'] == Chess.ROOK:
                board.rooks[data['id_pawn']] = data['new_field']
                board.save()
            elif data['pawn'] == Chess.KING:
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

        if data['command'] == Commands.FETCH_POSITONS:
            self.fetch_positions(data)
        elif data['command'] == Commands.MOVE_CHESS_PIECE:
            self.move_piece(data)
        else:
            raise Exception('socket receive wrong command!')

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

