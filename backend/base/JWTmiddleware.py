from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from urllib.parse import parse_qs
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import UntypedToken
from jwt import decode as jwt_decode
from django.conf import settings
from accounts.models import User
from django.db import close_old_connections

@database_sync_to_async
def get_user(id_user):
    try:
        return User.objects.get(id = id_user)
    except User.DoesNotExist:
        return AnonymousUser()


@database_sync_to_async
def close_connecton():
     close_old_connections()

class TokenAuthMiddleware(BaseMiddleware):

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        close_connecton()
        token = parse_qs(scope["query_string"].decode("utf8"))["token"][0]
        try:
            UntypedToken(token)
        except (InvalidToken, TokenError) as e:
            print(e)
            return None

        decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        scope['user'] = await get_user(decoded_data["user_id"])
        return await super().__call__(scope, receive, send)

