from django.db import models
from accounts.models import User
from chat.models import Chat
from django.shortcuts import get_object_or_404
from django.contrib.postgres.fields import ArrayField
from string import ascii_uppercase
from .chessSettings import Color, PiecesNameKeys, Positions, PieceMedia, ArrayFunc



class WhiteChessBoard(models.Model):

    owner = models.ForeignKey(User, related_name='white_chess_owner', null=True, blank=True, on_delete=models.CASCADE)
    pawns = ArrayField(models.PositiveIntegerField(), max_length=8, default=ArrayFunc.get_white_pawns)
    knights = ArrayField(models.PositiveIntegerField(), max_length=2, default=ArrayFunc.get_white_knights)
    queen = ArrayField(models.PositiveIntegerField(),max_length=1, default=ArrayFunc.get_white_queen)
    bishops = ArrayField(models.PositiveIntegerField(), max_length=2, default=ArrayFunc.get_white_bishops)
    rooks = ArrayField(models.PositiveIntegerField(), max_length=2, default=ArrayFunc.get_white_rooks)
    king = ArrayField(models.PositiveIntegerField(),
                            max_length=1, default=ArrayFunc.get_white_king)
    
        
class BlackChessBoard(models.Model):
    
    owner = models.ForeignKey(User, related_name='black_chess_owner', null=True, blank=True, on_delete=models.CASCADE)
    pawns = ArrayField(models.PositiveIntegerField(), max_length=8, default=ArrayFunc.get_black_pawns)
    knights = ArrayField(models.PositiveIntegerField(), max_length=2, default=ArrayFunc.get_black_knights)
    queen = ArrayField(models.PositiveIntegerField(), max_length=1, default=ArrayFunc.get_black_queen)
    bishops = ArrayField(models.PositiveIntegerField(), max_length=2, default=ArrayFunc.get_black_bishops)
    rooks = ArrayField(models.PositiveIntegerField(), max_length=2, default=ArrayFunc.get_black_rooks)
    king = ArrayField(models.PositiveIntegerField(),max_length=1, default=ArrayFunc.get_black_king)

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
    def next_turn(id):
        game = get_object_or_404(Game, id=id)
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
        json_pos[PiecesNameKeys.PAWN] = {
            'position': game.whiteChessBoard.pawns,
            'image': PieceMedia.WHITE_PAWN,
            'color': Color.WHITE
        }
        json_pos[PiecesNameKeys.KNIGHT] = {
            'position': game.whiteChessBoard.knights,
            'image': PieceMedia.WHITE_KNIGHT,
            'color': Color.WHITE
        }
        json_pos[PiecesNameKeys.QUEEN] = {
            'position': game.whiteChessBoard.queen,
            'image': PieceMedia.WHITE_QUEEN,
            'color': Color.WHITE
        }
        json_pos[PiecesNameKeys.BISHOP] = {
            'position': game.whiteChessBoard.bishops,
            'image': PieceMedia.WHITE_BISHOP,
            'color': Color.WHITE
        }
        json_pos[PiecesNameKeys.ROOK] = {
            'position': game.whiteChessBoard.rooks,
            'image': PieceMedia.WHITE_ROOK,
            'color': Color.WHITE
        }
        json_pos[PiecesNameKeys.KING] = {
            'position': game.whiteChessBoard.king,
            'image': PieceMedia.WHITE_KING,
            'color': Color.WHITE
        }

        return json_pos


    @staticmethod
    def get_black_pos(game):
        json_pos = {}
        json_pos[PiecesNameKeys.PAWN] = {
            'position': game.blackChessBoard.pawns,
            'image': PieceMedia.BLACK_PAWN,
            'color': Color.BLACK
        }
        json_pos[PiecesNameKeys.KNIGHT] = {
            'position': game.blackChessBoard.knights,
            'image': PieceMedia.BLACK_KNIGHT,
            'color': Color.BLACK
        }
        json_pos[PiecesNameKeys.QUEEN] = {
            'position': game.blackChessBoard.queen,
            'image': PieceMedia.BLACK_QUEEN,
            'color': Color.BLACK
        }
        json_pos[PiecesNameKeys.BISHOP] = {
            'position': game.blackChessBoard.bishops,
            'image': PieceMedia.BLACK_BISHOP,
            'color': Color.BLACK
        }
        json_pos[PiecesNameKeys.ROOK] = {
            'position': game.blackChessBoard.rooks,
            'image': PieceMedia.BLACK_ROOK,
            'color': Color.BLACK
        }
        json_pos[PiecesNameKeys.KING] = {
            'position': game.blackChessBoard.king,
            'image': PieceMedia.BLACK_KING,
            'color': Color.BLACK
        }

        return json_pos
