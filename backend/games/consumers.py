import json 
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Game, BlackChessBoard, WhiteChessBoard
from accounts.models import User
from django.shortcuts import get_object_or_404
from enum import Enum, auto
from .chessSettings import PiecesNameKeys, Color
from .chessMoves import PieceMoves as pm 

class frontend_backend_commands(str, Enum):
    FETCH_POSITONS = 'fetch_positions'
    MOVE_PIECE = 'move_piece'
    FETCH_REACHABLE_SQUARES = 'fetch_reachable_squares'
    REMOVE_PIECE = 'remove_piece'

class backend_frontend_commands(str, Enum):
    UPDATE_REACHABLE_SQUARES = 'squares'
    UPDATE_POSITIONS = 'positions'
    END_GAME = 'end'
    CHECK = 'check'
    UNCHACK = 'uncheck'

class GameConsumer(WebsocketConsumer):

    def fetch_positions(self, data):
        game = get_object_or_404(Game, id=data['gameId'])
        content = {
            'command': backend_frontend_commands.UPDATE_POSITIONS,
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
    
    def checkIfCheck(self, data, my_piece, enemies):
        tps = [[my_piece.pawns, PiecesNameKeys.PAWN],
               [my_piece.queen, PiecesNameKeys.QUEEN],
               [my_piece.knights, PiecesNameKeys.KNIGHT],
               [my_piece.bishops, PiecesNameKeys.BISHOP],
               [my_piece.rooks, PiecesNameKeys.ROOK]]
        
        # tak wiem to jest straszne!
        for tpy in tps:
            name = tpy[1]
            for pos in tpy[0]:
                _, attack = self.__get_moves_for_piece(pos, name, 
                                               my_piece, enemies, data['color'])
                
                for att in attack:
                    if att in enemies.king:
                        self.check()
                        return
                    else:
                        self.unCheck()
             

    def move_piece(self, data):
        game = get_object_or_404(Game, id=data['gameId'])

        if data['color'] == Color.WHITE:
            my_piece = game.whiteChessBoard
            enemies = game.blackChessBoard 
        elif data['color'] == Color.BLACK:
            my_piece = game.blackChessBoard
            enemies = game.whiteChessBoard 

        if game.who_has_turn == self.user:
            if data['color'] == Color.WHITE:
                board = game.whiteChessBoard
            elif data['color'] == Color.BLACK:
                board = game.blackChessBoard 
            else:
                raise Exception('missing color!')

            self.__update_piece_positons(data, board)
            self.checkIfCheck(data, my_piece, enemies)
             
            Game.next_turn(game.id)

        content = {
            'command': backend_frontend_commands.UPDATE_POSITIONS,
            'white_pos': Game.get_white_pos(game),
            'black_pos': Game.get_black_pos(game)
        }
        self.send_to_game(content)
    

    def __get_moves_for_piece(self, pos, name, my_piece, enemies, color):
        if name == PiecesNameKeys.PAWN:
            if color == Color.WHITE:
                return pm.get_white_pawn_moves(pos, my_piece, enemies)
            if color == Color.BLACK:
                return pm.get_black_pawn_moves(pos, my_piece, enemies)

        elif name == PiecesNameKeys.BISHOP:
            return pm.get_bishop_moves(pos, my_piece, enemies)
        elif name == PiecesNameKeys.ROOK:
            return pm.get_rook_moves(pos, my_piece, enemies)
        elif name == PiecesNameKeys.QUEEN:
            return pm.get_queen_moves(pos, my_piece, enemies)
        elif name == PiecesNameKeys.KING:
            return pm.get_king_moves(pos, my_piece, enemies)
        elif name == PiecesNameKeys.KNIGHT:
            return pm.get_knight_moves(pos, my_piece, enemies)
    

    def get_reachable_squares(self, data):
        game = get_object_or_404(Game, id=data['gameId'])
        if data['color'] == Color.WHITE:
            my_piece = game.whiteChessBoard
            enemies = game.blackChessBoard 
        elif data['color'] == Color.BLACK:
            my_piece = game.blackChessBoard
            enemies = game.whiteChessBoard 
        else:
            raise Exception('chess with that color not exist!')
        
        if my_piece.owner != self.user or game.who_has_turn != self.user:
            return  

        moves, attack = self.__get_moves_for_piece(data['pos'], data['name'], 
                                           my_piece, enemies, data['color'])
        content = {
            'command': backend_frontend_commands.UPDATE_REACHABLE_SQUARES,
            'reachable_squares': moves,
            'attack_squares': attack,
            'oldPos': data['pos'],
            'color': data['color'],
            'name': data['name']
        }
        self.send_to_game(content)


    def end_game(self, data, winner):
        Game.mark_complete(data['gameId'], winner.id)
        content = {
            'command': backend_frontend_commands.END_GAME,
            'winner' : winner
        }
        self.send_to_game(content)
    
    def check(self):
        content = {
            'command': backend_frontend_commands.CHECK,
        }
        self.send_to_game(content)

    def unCheck(self):
        content = {
            'command': backend_frontend_commands.UNCHACK,
        }
        self.send_to_game(content)

    def remove_piece(self, data):
        game = get_object_or_404(Game, id=data['gameId'])
        if data['color'] == Color.WHITE:
            print('color: ',data['color'])
            my_piece = game.whiteChessBoard
            enemies = game.blackChessBoard 
        elif data['color'] == Color.BLACK:
            print('color: ',data['color'])
            my_piece = game.blackChessBoard
            enemies = game.whiteChessBoard 
        else:
            raise Exception('chess with that color not exist!')
        
        if data['pos'] in enemies.pawns:
            enemies.pawns.remove(data['pos'])

        if data['pos'] in enemies.bishops:
            enemies.bishops.remove(data['pos'])

        if data['pos'] in enemies.rooks:
            enemies.rooks.remove(data['pos'])

        if data['pos'] in enemies.queen:
            enemies.queen.remove(data['pos'])

        if data['pos'] in enemies.king:
            enemies.king.remove(data['pos'])
            self.end_game(data, self.user)

        if data['pos'] in enemies.knights:
            enemies.knights.remove(data['pos'])
    
        enemies.save()
        game.save()
        my_piece.save()
       
        self.move_piece(data)



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
        elif data['command'] == frontend_backend_commands.MOVE_PIECE:
            self.move_piece(data)
        elif data['command'] == frontend_backend_commands.FETCH_REACHABLE_SQUARES:
            self.get_reachable_squares(data)
        elif data['command'] == frontend_backend_commands.REMOVE_PIECE:
            self.remove_piece(data)
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

