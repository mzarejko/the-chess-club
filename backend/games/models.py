from django.db import models
from accounts.models import User
from chat.models import Chat

class Game(models.Model):
    author = models.ForeignKey(User, related_name='author', null=False, on_delete=models.CASCADE)
    opponent = models.ForeignKey(User, related_name='opponent', null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now_add=True)
    winner = models.ForeignKey(User, related_name='winner', null=True, blank=True, on_delete=models.SET_NULL)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    
