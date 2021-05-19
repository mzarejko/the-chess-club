from django.db import models
from accounts.models import User
from chat.models import Chat
from django.shortcuts import get_object_or_404
from django.contrib.postgres.fields import ArrayField
from string import ascii_uppercase
from  . import chessPos 
from . import chessImageAPI 
from .chessName import Pieces



class WhiteChessBoard(models.Model):

    owner = models.ForeignKey(User, related_name='white_chess_owner', null=True, blank=True, on_delete=models.CASCADE)
    pawns = ArrayField(models.PositiveIntegerField(), max_length=8, default=chessPos.get_white_pawns)
    knights = ArrayField(models.PositiveIntegerField(), max_length=2, default=chessPos.get_white_knights)
    queen = ArrayField(models.PositiveIntegerField(),max_length=1, default=chessPos.get_white_queen)
    bishops = ArrayField(models.PositiveIntegerField(), max_length=2, default=chessPos.get_black_bishops)
    rooks = ArrayField(models.PositiveIntegerField(), max_length=2, default=chessPos.get_white_rooks)
    king = ArrayField(models.PositiveIntegerField(),
                            max_length=1, default=chessPos.get_white_king)
        
class BlackChessBoard(models.Model):
    
    owner = models.ForeignKey(User, related_name='black_chess_owner', null=True, blank=True, on_delete=models.CASCADE)
    pawns = ArrayField(models.PositiveIntegerField(), max_length=8, default=chessPos.get_black_pawns)
    knights = ArrayField(models.PositiveIntegerField(), max_length=2, default=chessPos.get_black_knights)
    queen = ArrayField(models.PositiveIntegerField(), max_length=1, default=chessPos.get_black_queen)
    bishops = ArrayField(models.PositiveIntegerField(), max_length=2, default=chessPos.get_black_bishops)
    rooks = ArrayField(models.PositiveIntegerField(), max_length=2, default=chessPos.get_black_rooks)
    king = ArrayField(models.PositiveIntegerField(),max_length=1, default=chessPos.get_black_king)

class Game(models.Model):
    author = models.ForeignKey(User, related_name='author', null=False, on_delete=models.CASCADE)
    opponent = models.ForeignKey(User, related_name='opponent', null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now_add=True)
    winner = models.ForeignKey(User, related_name='winner', null=True, blank=True, on_delete=models.SET_NULL)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    who_has_turn = models.ForeignKey(User, related_name='hasTurn', null=True, blank=True, on_delete=models.CASCADE)
    whiteChessBoard = models.ForeignKey(WhiteChessBoard, null=True, related_name='white_chess', on_delete=models.CASCADE)
    blackChessBoard = models.ForeignKey(BlackChessBoard, null=True, related_name='black_chess', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    

    @staticmethod
    def get_user_turn(id_game):
        game = get_object_or_404(Game, id=id_game)
        return game.who_has_turn 

    @staticmethod
    def next_turn(id_game):
        game = get_object_or_404(Game, id=id_game)
        if game.who_has_turn == game.author:
            game.who_has_turn = game.opponent 
        elif game.who_has_turn == game.opponent:
            game.who_has_turn = game.author
        game.save()

    @staticmethod
    def mark_complete(id_game, user):
        game = get_object_or_404(Game, id=id_game)
        game.winner = user
        game.save()
        
    @staticmethod
    def get_white_pos(game):
        json_pos = {}
        json_pos[Pieces.PAWN] = {
            'position': game.whiteChessBoard.pawns,
            'image': chessImageAPI.WHITE_PAWN
        }
        json_pos[Pieces.KNIGHT] = {
            'position': game.whiteChessBoard.knights,
            'image': chessImageAPI.WHITE_KNIGHT
        }
        json_pos[Pieces.QUEEN] = {
            'position': game.whiteChessBoard.queen,
            'image': chessImageAPI.WHITE_QUEEN
        }
        json_pos[Pieces.BISHOP] = {
            'position': game.whiteChessBoard.bishops,
            'image': chessImageAPI.WHITE_BISHOP
        }
        json_pos[Pieces.ROOK] = {
            'position': game.whiteChessBoard.rooks,
            'image': chessImageAPI.WHITE_ROOK
        }
        json_pos[Pieces.KING] = {
            'position': game.whiteChessBoard.king,
            'image' : chessImageAPI.WHITE_KING
        }

        return json_pos


    @staticmethod
    def get_black_pos(game):
        json_pos = {}
        json_pos[Pieces.PAWN] = {
            'position': game.blackChessBoard.pawns,
            'image': chessImageAPI.BLACK_PAWN 
        }
        json_pos[Pieces.KNIGHT] = {
            'position': game.blackChessBoard.knights,
            'image': chessImageAPI.BLACK_KNIGHT 
        }
        json_pos[Pieces.QUEEN] = {
            'position': game.blackChessBoard.queen,
            'image': chessImageAPI.BLACK_QUEEN
        }
        json_pos[Pieces.BISHOP] = {
            'position': game.blackChessBoard.bishops,
            'image': chessImageAPI.BLACK_BISHOP
        }
        json_pos[Pieces.ROOK] = {
            'position': game.blackChessBoard.rooks,
            'image': chessImageAPI.BLACK_ROOK
        }
        json_pos[Pieces.KING] = {
            'position': game.blackChessBoard.king,
            'image' : chessImageAPI.BLACK_KING
        }

        return json_pos
