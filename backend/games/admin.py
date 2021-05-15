from django.contrib import admin
from .models import Game, ChessBoard

admin.site.register([Game, ChessBoard])
