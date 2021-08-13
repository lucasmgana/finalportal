from django.contrib.auth.views import LoginView
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm


app_name = "clients"

urlpatterns = [    
    path('register/', UserRegisterView.as_view(), name='register'),
    path('user-profile/<int:pk>', ProfileView.as_view(), name = 'profile'),
    path('edit-profile/', UserEditProfile.as_view(), name = 'editprofile'),
    path('password/', PasswordsChangeView.as_view(template_name='clients/change-password.html'), name = 'change-password'),
]
