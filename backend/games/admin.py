from django.contrib import admin
from .models import Game, WhiteChessBoard, BlackChessBoard

admin.site.register([Game, WhiteChessBoard, BlackChessBoard])
