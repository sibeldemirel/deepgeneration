from json import load
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page),
    path('image/', views.image_page),
    path('blog/', views.blog_page),
    path('code/', views.code_page),
]