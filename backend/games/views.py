from .models import Game 
from .serializers import GameSerializer, GameListSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny 
from accounts.models import User
from django.db.models import Q
from chat.models import Chat
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status 
from .filter_class import GameFilter
from chat.models import Chat
from .models import WhiteChessBoard, BlackChessBoard
import random
from django.shortcuts import get_object_or_404
from enum import Enum, auto
from .permissions import IsGameNotCompleted

class color_chess(Enum):
    BLACK = auto()
    WHITE = auto()

# create game with author
class CreateGame(CreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = GameSerializer 

    def perform_create(self, serializer):
        author = self.request.user
        chat = Chat.objects.create()
        chat.members.add(self.request.user)
        chat.save()
        white_chess = WhiteChessBoard.objects.create()
        white_chess.save()
        black_chess = BlackChessBoard.objects.create()
        black_chess.save()
        return serializer.save(author=author, 
                               chat=chat, 
                               whiteChessBoard=white_chess,
                               blackChessBoard=black_chess)


class ListGamesInWaitingRoom(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = GameListSerializer
    filterset_class = GameFilter 

    def get_queryset(self):
        games = Game.objects.all()
        return games


class JoinToGame(APIView):
    permission_classes = [IsAuthenticated, IsGameNotCompleted]

    def draw_color(self,game):
        white_chess = get_object_or_404(WhiteChessBoard, id=game.whiteChessBoard.id)
        black_chess = get_object_or_404(BlackChessBoard, id=game.blackChessBoard.id)

        color = random.choice([color_chess.BLACK, color_chess.WHITE])
        if color == color_chess.BLACK:
            white_chess.owner = game.author
            game.who_has_turn = game.author
            black_chess.owner = game.opponent
            
        else:
            white_chess.owner = game.opponent
            game.who_has_turn = game.opponent
            black_chess.owner = game.author

        white_chess.save()
        black_chess.save()
        game.save()

    def put(self, request, pk):
        game = get_object_or_404(Game, id=pk)
        # add user to chat
        if not Chat.objects.filter(members=self.request.user).exists():
            game.chat.members.add(request.user)

        if not game.opponent and self.request.user != game.author:
            opponent = request.user 
            game.opponent = opponent
            game.save()

            self.draw_color(game)
        else:
            return Response({'success': 'You have been attached to the chat'}, status=status.HTTP_200_OK)
        return Response({'success': 'You have been attached to the game as opponent'}, status=status.HTTP_200_OK)


