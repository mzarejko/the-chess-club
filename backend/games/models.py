from django.db import models
from accounts.models import User
from chat.models import Chat
from django.shortcuts import get_object_or_404
from django.contrib.postgres.fields import ArrayField
from string import ascii_uppercase
from  . import chessPos 

class WhiteChessBoard(models.Model):

    owner = models.ForeignKey(User, related_name='white-chess-owner', null=True, blank=True, on_delete=models.CASCADE)
    pawns = ArrayField(ArrayField(models.PositiveIntegerField(), 
                            max_length=2), max_length=8, default=chessPos.get_white_pawns)
    knights = ArrayField(ArrayField(models.PositiveIntegerField(),
                            max_length=2), max_length=2, default=chessPos.get_white_knights)
    queen = ArrayField(models.PositiveIntegerField(),
                             max_length=2, default=chessPos.get_white_queen)
    bishops = ArrayField(ArrayField(models.PositiveIntegerField(),
                             max_length=2), max_length=2, default=chessPos.get_black_bishops)
    rooks = ArrayField(ArrayField(models.PositiveIntegerField(),
                            max_length=2), max_length=2, default=chessPos.get_white_rooks)
    king = ArrayField(models.PositiveIntegerField(),
                            max_length=2, default=chessPos.get_white_king)
        
class BlackChessBoard(models.Model):
    
    owner = models.ForeignKey(User, related_name='black-chess-owner', null=True, blank=True, on_delete=models.CASCADE)
    pawns = ArrayField(ArrayField(models.PositiveIntegerField(),
                                        max_length=2), max_length=8, default=chessPos.get_black_pawns)
    knights = ArrayField(ArrayField(models.PositiveIntegerField(), 
                            max_length=2), max_length=2, default=chessPos.get_black_knights)
    queen = ArrayField(models.PositiveIntegerField(), 
                             max_length=2, default=chessPos.get_black_queen)
    bishops = ArrayField(ArrayField(models.PositiveIntegerField(),
                             max_length=2), max_length=2, default=chessPos.get_black_bishops)
    rooks = ArrayField(ArrayField(models.PositiveIntegerField(),
                            max_length=2), max_length=2, default=chessPos.get_black_rooks)
    king = ArrayField(models.PositiveIntegerField(),
                            max_length=2, default=chessPos.get_black_king)

class Game(models.Model):
    author = models.ForeignKey(User, related_name='author', null=False, on_delete=models.CASCADE)
    opponent = models.ForeignKey(User, related_name='opponent', null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now_add=True)
    winner = models.ForeignKey(User, related_name='winner', null=True, blank=True, on_delete=models.SET_NULL)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    who_has_turn = models.ForeignKey(User, related_name='hasTurn', null=True, blank=True, on_delete=models.CASCADE)
    whiteChessBoard = models.ForeignKey(WhiteChessBoard, related_name='white-chess', on_delete=models.CASCADE)
    blackChessBoard = models.ForeignKey(BlackChessBoard, related_name='black-chess', on_delete=models.CASCADE)
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
        json_pos = [{'pawns': game.whiteChessBoard.pawns,
                     'knights': game.whiteChessBoard.knights,
                     'queen': game.whiteChessBoard.queen,
                     'bishops': game.whiteChessBoard.bishops,
                     'rooks': game.whiteChessBoard.rooks,
                     'king': game.whiteChessBoard.king}]
        return json_pos

    @staticmethod
    def get_black_pos(game):
        json_pos = [{'pawns': game.blackChessBoard.pawns,
                     'knights': game.blackChessBoard.knights,
                     'queen': game.blackChessBoard.queen,
                     'bishops': game.blackChessBoard.bishops,
                     'rooks': game.blackChessBoard.rooks,
                     'king': game.blackChessBoard.king}]
        return json_pos
