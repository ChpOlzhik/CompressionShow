from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.mainPage, name='main'),
    path('encoded', views.encode, name='encode'),


]
