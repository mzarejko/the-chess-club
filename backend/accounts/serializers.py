from rest_framework import serializers
from .models import User 
from django.contrib.auth import get_user_model 
from django.contrib import auth
from rest_framework import status 
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

  
class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, allow_null=False)
    email = serializers.EmailField(required=True, allow_null=False)
    password1 = serializers.CharField(required=True, write_only=True,
                                      style={'input_type': 'password'})

    password2 = serializers.CharField(required=True, write_only=True,
                                      style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        
    # extended function for create user
    def create(self, data):
        password1 = data['password1'] 
        password2 = data['password2'] 


        if password1 != password2:
            raise ValidationError({'error': "passwords not match"})

        # check if user already exist but is not verfied yet
        if User.objects.filter(username=data['username'], email=data['email'], 
                               is_verified=False).exists():

            return User.objects.get(username=data['username'], email=data['email'])
        elif User.objects.filter(email=data['email'], is_verified=False).exists():
            raise ValidationError({'error': "email already have account"}, 
                                  code=status.HTTP_409_CONFLICT)
        elif not User.objects.filter(email=data['email']).exists():

            user = User(
                username=data['username'],
                email=data['email'],
            )
            user.set_password(password1)
            user.save()
            return user
        raise ValidationError({'error': "email already have account"}, 
                                  code=status.HTTP_409_CONFLICT)

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=45, required=True, write_only=True)
    password = serializers.CharField(max_length=45, write_only=True, required=True)
    access = serializers.CharField(max_length=45, read_only=True)
    refresh = serializers.CharField(max_length=45, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'access', 'refresh']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is None:
            raise ValidationError('wrong password or email',
                                  code=status.HTTP_400_BAD_REQUEST)
        
        if not user.is_active:
            raise ValidationError('Account not active',
                                  code=status.HTTP_406_NOT_ACCEPTABLE)

        if not user.is_verified:
            raise ValidationError('Account not verfied, first active your profile',
                                  code=status.HTTP_400_BAD_REQUEST)

        tokens = user.tokens()
        return {"access": tokens['access'],
                "refresh": tokens['refresh']} 
                        
class ResetPasswordSerializer(serializers.Serializer):
    email=serializers.EmailField(max_length=45, required=True)
    
    class Meta:
        fields = ['email']

class SetNewPasswordSerializer(serializers.Serializer):
    password1 = serializers.CharField(max_length=68, write_only=True)
    password2 = serializers.CharField(max_length=68, write_only=True)
    token = serializers.CharField(write_only=True)
    uidb64 = serializers.CharField(write_only=True)

    class Meta:
        fields = ['password1', 'password2', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password1 = attrs.get('password1')
            password2 = attrs.get('password2')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)
            
            if password1 == password2:
                user.set_password(password1)
                user.save()
                return user
            else:
                raise ValidationError('passwords are not the same!', code=status.HTTP_406_NOT_ACCEPTABLE)
        except:
            raise ValidationError('bad request, check if url is right', code=status.HTTP_400_BAD_REQUEST)
        return super().validate(attrs)
