import json 
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Game, BlackChessBoard, WhiteChessBoard
from accounts.models import User
from django.shortcuts import get_object_or_404
from enum import Enum, auto
from .chessSettings import PiecesNameKeys, Color
from .chessMoves import MovePiece

class frontend_backend_commands(str, Enum):
    FETCH_POSITONS = 'fetch_positions'
    MOVE_CHESS_PIECE = 'move_piece'
    GET_REACHABLE_SQUARE = 'get_reachable_squares'

class backend_frontend_commands(str, Enum):
    SEND_REACHABLE_SQUARES = 'squares'
    SEND_NEW_POSITIONS = 'positions'

class GameConsumer(WebsocketConsumer):

    def fetch_positions(self, data):
        game = get_object_or_404(Game, id=data['gameId'])
        content = {
            'command': backend_frontend_commands.SEND_NEW_POSITIONS,
            'white_pos': Game.get_white_pos(game),
            'black_pos': Game.get_black_pos(game)
        }
        self.send_to_frontend(content)
    
    def __update_piece_positons(self, data, board):
        if data['name'] == PiecesNameKeys.PAWN:
            if data['old_pos'] in board.pawns:
               id = board.pawns.index(data['old_pos']) 
               board.pawns[id] = data['pos']
               board.save()
        elif data['name'] == PiecesNameKeys.BISHOP:
            if data['old_pos'] in board.bishops:
               id = board.bishops.index(data['old_pos']) 
               board.bishops[id] = data['pos']
               board.save()
        elif data['name'] == PiecesNameKeys.KING:
            if data['old_pos'] in board.king:
               id = board.king.index(data['old_pos']) 
               board.king[id] = data['pos']
               board.save()
        elif data['name'] == PiecesNameKeys.ROOK:
            if data['old_pos'] in board.rooks:
               id = board.rooks.index(data['old_pos']) 
               board.rooks[id] = data['pos']
               board.save()
        elif data['name'] == PiecesNameKeys.QUEEN:
            if data['old_pos'] in board.queen:
               id = board.queen.index(data['old_pos']) 
               board.queen[id] = data['pos']
               board.save()
        elif data['name'] == PiecesNameKeys.KNIGHT:
            if data['old_pos'] in board.knights:
               id = board.knights.index(data['old_pos']) 
               board.knights[id] = data['pos']
               board.save()

    def move_piece(self, data):
        game = get_object_or_404(Game, id=data['gameId'])
        if game.who_has_turn == self.user:
            if data['color'] == Color.WHITE:
                board = game.whiteChessBoard
            elif data['color'] == Color.BLACK:
                board = game.blackChessBoard 
            else:
                raise Exception('missing color!')

            self.__update_piece_positons(data, board)
            Game.next_turn(game.id)

        content = {
            'command': backend_frontend_commands.SEND_NEW_POSITIONS,
            'white_pos': Game.get_white_pos(game),
            'black_pos': Game.get_black_pos(game)
        }
        self.send_to_game(content)
    

    def __get_moves_for_piece(self, pos, name, board, color):
        if name == PiecesNameKeys.PAWN:
            position = board.pawns
            if pos in position:
                if color == Color.WHITE:
                    return MovePiece.get_white_pawn_moves(pos, board)
                if color == Color.BLACK:
                    return MovePiece.get_black_pawn_moves(pos, board)

        elif name == PiecesNameKeys.BISHOP:
            position = board.bishops
            if pos in position:
                return MovePiece.get_bishop_moves(pos, board)
        elif name == PiecesNameKeys.ROOK:
            position = board.rooks
            if pos in position:
                return MovePiece.get_rook_moves(pos, board)
        elif name == PiecesNameKeys.QUEEN:
            position = board.queen
            if pos in position:
                return MovePiece.get_queen_moves(pos, board)
        elif name == PiecesNameKeys.KING:
            position = board.king
            if pos in position:
                return MovePiece.get_king_moves(pos, board)
        elif name == PiecesNameKeys.KNIGHT:
            position = board.knights
            if pos in position:
                return MovePiece.get_knight_moves(pos, board)
    

    def get_reachable_squares(self, data):
        game = get_object_or_404(Game, id=data['gameId'])
        if data['color'] == Color.WHITE:
            board = game.whiteChessBoard
        elif data['color'] == Color.BLACK:
            board = game.blackChessBoard
        else:
            raise Exception('chess with that color not exist!')
        
        print(board.owner)
        print(self.user)
        print(game.who_has_turn)
        if board.owner != self.user or game.who_has_turn != self.user:
            return  

        moves = self.__get_moves_for_piece(data['position'], data['name'], board, data['color'])
        content = {
            'command': backend_frontend_commands.SEND_REACHABLE_SQUARES,
            'squares': moves,
            'oldPos': data['position'],
            'color': data['color'],
            'name': data['name']
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

        if data['command'] == frontend_backend_commands.FETCH_POSITONS:
            self.fetch_positions(data)
        elif data['command'] == frontend_backend_commands.MOVE_CHESS_PIECE:
            self.move_piece(data)
        elif data['command'] == frontend_backend_commands.GET_REACHABLE_SQUARE:
            self.get_reachable_squares(data)
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

