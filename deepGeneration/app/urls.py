from json import load
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name = 'url_home'),
    path('image/', views.image_page, name = 'url_image'),
    path('code/', views.code_page, name = 'url_code'),
    path('blog/', views.blog_page, name = 'url_blog'),
    path('article/', views.article_page, name = 'url_article'),
    path('contact/', views.contact_page, name = 'url_contact'),
    path('signup/', views.SignupPage.as_view(), name='signup'),
]