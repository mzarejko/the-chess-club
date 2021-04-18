from django.urls import path
from . import views 
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', views.RegisterAPI.as_view(), name='register'),
    path('email-verify', views.VerifyEmail.as_view(), name='verify'),
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),
    path('logout/', views.LogoutAPI.as_view(), name='logout'),
    path('users/', views.GetUsers.as_view(), name='users'),
    path('reset-password/<uidb64>/<token>/', views.TokenRegisterCheckAPI.as_view(), name='token-check'),
    path('reset-password-email/', views.PasswordResetAPI.as_view(), name='reset-passwd'),
    path('reset-password-complete/', views.SetNewPasswordAPI.as_view(), name='new-passwd'),
]

