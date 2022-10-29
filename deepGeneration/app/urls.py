from json import load
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page, name = 'url_home'),
    path('image/', views.image_page, name = 'url_image'),
    path('code/', views.code_page, name = 'url_code'),
    path('blog/', views.blog_page, name = 'url_blog'),
    path('article/', views.article_page, name = 'url_article'),
    path('contact/', views.contact_page, name = 'url_contact'),
    path('special/', views.special_page, name = 'url_special'),
    path('list/', views.ModelListView.as_view(), name = 'url_requestsList'),
    path('signup/', views.signup_page, name = 'url_signup'),
    path('login/', views.login_page, name = 'url_login'),
]