from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken


# this is needed because we extend AbstractBaseUser  
class CustomAccountManager(BaseUserManager):

    def create_superuser(self, username, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be superuser')

        return self.create_user(username, email, password, **other_fields)

    def create_user(self, username, email, password, **other_fields):
        
        if username is None:
            raise TypeError('Users shuld have a username')
        if email is None:
            raise TypeError('Users shuld have emali')

        email = self.normalize_email(email)
        
        user = self.model(username=username, email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
         
    def tokens(self):
        token=RefreshToken.for_user(self)
        return {"access": str(token.access_token),
                "refresh": str(token)}
        
