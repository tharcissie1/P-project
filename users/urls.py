from django.urls import path
from django.contrib import admin
from .import views
from django.contrib.auth import views as auth_views




urlpatterns = [
   
 path('update/', views.update_user, name='update'),
 ]

