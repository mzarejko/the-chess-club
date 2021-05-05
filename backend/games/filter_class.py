from django_filters import rest_framework as filters, CharFilter
from .models import Game
from rest_framework import serializers
from accounts.serializers import UsernameSerializer 
from accounts.models import User

class GameFilter(filters.FilterSet):

    class Meta:
        model = Game
        fields = ['author__username', 'opponent__username', 'winner__username']
    

