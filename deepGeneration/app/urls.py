from json import load
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page, name = 'url_home'),
    path('image/', views.image_page, name = 'url_image'),
    path('code/', views.code_page, name = 'url_code'),
    path('codeArticle/', views.code_article_page, name = 'url_codeArticle'),
    path('article/', views.article_page, name = 'url_article'),
    path('profil/', views.profil_page, name = 'url_profil'),
    path('list/', views.ModelListView.as_view(), name = 'url_requestsList'),
    path('signup/', views.SignUpPage.as_view(), name = 'url_signUp'),
    path('recent/', views.articles_recent, name = 'url_blog'),
    path('contact/', views.contact_page, name = 'url_contact'),
    path('image<int:id>', views.imageDetail_page, name = 'url_imageDetail'),
    path('article<int:id>', views.articleDetail_page, name = 'url_articleDetail'),
    path('code<int:id>', views.codeDetail_page, name = 'url_codeDetail'),
]