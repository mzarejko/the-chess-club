from django.urls import path
from . import views 

urlpatterns = [
    path('', views.ListGamesInWaitingRoom.as_view(), name='games'),
    path('<int:pk>/', views.JoinToAnonymusGame.as_view(), name='join-anonymus'),
    path('new/', views.CreateGame.as_view(), name='new-game'),
]
