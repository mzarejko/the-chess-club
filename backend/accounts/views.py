from .models import User  
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from django.http import Http404 
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.sites.shortcuts import get_current_site 
from django.urls import reverse 
import jwt
from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListAPIView
from .filter_class import UsernameFilter
from django.core.mail import EmailMessage 
from .tasks import send_emali
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

class GetUsers(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.UsernameSerializer
    filterset_class = UsernameFilter 

    def get_queryset(self):
        users = User.objects.all()
        return users

class LoginAPI(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)

class RegisterAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            user = User.objects.get(email=serializer.data['email'])
            token = RefreshToken.for_user(user).access_token

            current_site = get_current_site(request).domain
            relativeLink = reverse('verify')
            absurl = 'http://'+current_site+relativeLink+"?token="+str(token)

            email_body = f'Hi {user.username} click this link to active account:  \n {absurl}'
            mail = {'text': email_body, 'who': user.email, 'header': 'Verify your email'}

            send_emali(mail)
            return Response("Check your mail for activation mail", status=status.HTTP_201_CREATED)

class VerifyEmail(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        token = request.GET.get('token')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()

            return Response('Successfully activated', status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response('token expired', status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError:
            return Response('invalid token', status=status.HTTP_400_BAD_REQUEST)

class LogoutAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            RefreshToken(refresh_token).blacklist()
        except TokenError:
            return Response('Token is invalid or expired')
        return Response('Successful logout', status=status.HTTP_204_NO_CONTENT)



class PasswordResetAPI(generics.GenericAPIView):
    serializer_class = serializers.ResetPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request.data.get('email', '')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64= urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            
            current_site = get_current_site(request=request).domain
            relativeLink=reverse('token-check', kwargs={'uidb64': uidb64, 'token': token})
            absurl='http://'+current_site+relativeLink
            email_body = f'Hi {user.username} click this link to reset password:  \n {absurl}'
            mail = {'text': email_body, 'who': user.email, 'header': 'The chess club - reset password'}
            send_emali(mail)

        return Response('Check your mail, there should be reset password link', status=status.HTTP_200_OK)


class TokenRegisterCheckAPI(generics.GenericAPIView):
    serializer_class = serializers.SetNewPasswordSerializer
    permission_classes = [AllowAny]

    def get(self, request, uidb64, token):
        try:
            # return in string bytes id of user
            id=smart_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=id)
            
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response('token has expired or is not valid', status=status.HTTP_401_UNAUTHORIZED)
            return Response({'success': True, 'message': 'credentials valid', 'uidb64': uidb64, 'token': token}, status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response('token is not valid', status=status.HTTP_401_UNAUTHORIZED)


class SetNewPasswordAPI(generics.GenericAPIView):
    serializer_class = serializers.SetNewPasswordSerializer
    permission_classes = [AllowAny]

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)



