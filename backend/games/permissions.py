from rest_framework import permissions
from .models import Game 

class IsGameNotCompleted(permissions.BasePermission):
    message="This game already end, you can't join there"

    def has_object_permission(self, request, view, obj):
        return obj.completed
