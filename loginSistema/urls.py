from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, logout_then_login

from .views import login_view, logout_view

app_name = 'loginSistema'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
