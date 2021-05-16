from channels.routing import ProtocolTypeRouter, URLRouter 
from .JWTmiddleware import TokenAuthMiddleware  
import chat.routing
import games.routing 
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.urls import re_path

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": TokenAuthMiddleware(
        URLRouter(
            chat.routing.websocket_urlpatterns+
            games.routing.websocket_urlpatterns
        )
    )

})
