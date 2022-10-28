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
    path('special/', views.special_page, name = 'url_special'),
    path('list/', views.ModelListView.as_view(), name = 'url_requestsList'),
    path('signup/', views.SignUpPage.as_view(), name = 'url_signup'),
]