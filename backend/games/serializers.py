from rest_framework import serializers
from .models import Game 
from accounts.serializers import UsernameSerializer 
from accounts.models import User

class GameListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    winner = serializers.SerializerMethodField()
    opponent = serializers.SerializerMethodField()
    date=serializers.DateField(format="%d:%m:%Y")
    
    
    class Meta:
        model= Game
        fields = ['pk', 'winner', 'author', 'opponent', 'date', 'chat']


    def get_author(self, game):
        return game.author.username

    def get_winner(self, game):
        if game.winner:
            return game.winner.username
        else:
            return 'undefine'

    def get_opponent(self, game):
        if game.opponent:
            return game.opponent.username
        else:
            return 'undefine'

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ['opponent', 'date', 'winner']


