from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError, PermissionDenied, NotAuthenticated, AuthenticationFailed
from django.http import Http404 
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render


def custome_exception_handler(exc, context):    
    response = exception_handler(exc, context)

    if isinstance(exc, ValidationError):
        create_validate_error(exc, context, response)
    elif isinstance(exc, PermissionDenied):
        create_permission_error(exc, context, response)
    elif isinstance(exc, NotAuthenticated):
        create_authentication_error(exc, context, response)
    elif isinstance(exc, Http404):
        create_404(response)
    elif isinstance(exc, AuthenticationFailed):
        token_expired(response)

    return response 

def create_validate_error(exc, context, response):
    return response

def create_permission_error(exc, context, response):
    return response

def create_authentication_error(exc, context,response):
    return response 

def create_404(response):
    return response

def token_expired(response):
    return response
