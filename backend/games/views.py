from .models import Game 
from .serializers import GameSerializer, GameListSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny 
from accounts.models import User
from django.db.models import Q
from chat.models import Chat
from rest_framework.views import APIView 
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status 
from .filter_class import GameFilter
from chat.models import Chat

# create game with author
class CreateGame(CreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = GameSerializer 

    def perform_create(self, serializer):
        author = self.request.user
        chat = Chat.objects.create()
        chat.members.add(self.request.user)
        chat.save()
        return serializer.save(author=author, chat=chat)


class ListGamesInWaitingRoom(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = GameListSerializer
    filterset_class = GameFilter 

    def get_queryset(self):
        games = Game.objects.all()
        return games


class JoinToAnonymusGame(APIView):
    permission_classes = [AllowAny]
    
    def get_game(self, pk):
        try:
            game = Game.objects.get(pk=pk, opponent=None)
        except Game.DoesNotExist:
            raise Http404 
        return game


    def put(self, request, pk):
        game = self.get_game(pk)
        # add user to chat
        if not Chat.objects.filter(members=self.request.user).exists():
            game.chat.members.add(request.user)

        if not game.opponent and self.request.user != game.author:
            opponent = request.user 
            game.opponent = opponent
            game.save()
        else:
            return Response({'success': 'You have been attached to the chat'}, status=status.HTTP_200_OK)
        return Response({'success': 'You have been attached to the game as opponent'}, status=status.HTTP_200_OK)

        

