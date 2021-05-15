from django.urls import path
from . import views 

urlpatterns = [
    path('', views.ListGamesInWaitingRoom.as_view(), name='games'),
    path('<int:pk>/', views.JoinToGame.as_view(), name='join'),
    path('new/', views.CreateGame.as_view(), name='new-game'),
]
