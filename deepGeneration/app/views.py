from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout

from .management.commands import generator, user
from . import forms, models
from os import getenv

user = user.User()
gen = generator.Generator(user)

def home_page(request):
    title = "Accueil"
    context = {"title" : title}
    return render(request, 'app/home.html', context = context)

def articles_recent(request) :
    title = "Articles Récents"
    articles = models.ArticleModel.objects.all()#filter(article_date= "2022-10-28") # ajouter filtre date utilisateur
    # request.session['article'] = article
    # request.session['title'] = title
    # request.session['image'] = image  
    context = {"title" : title, "articles" : articles}
    return render(request, 'app/recent_articles.html', context = context)


def getDescription(request):
    form = forms.ApiForm(request.POST)
    if form.is_valid() :
        description = form.cleaned_data['description']
        return description

def article_page(request):
    title = request.session['title']
    article = request.session['article']
    context = {"article" : article, 'title' : title}
    return render(request, 'app/article.html', context = context)

def code_article_page(request):
    title = "Article Generator"
    if request.method =="POST" :
        # form.save()
        description = getDescription(request)
        article = gen.generateArticle(description)
        request.session['article'] = article
        request.session['title'] = title
        context = {"title" : title, 'article' : article}
        return render(request, 'app/code_article.html', context = context)
    else :
            form = forms.ApiForm()
            context = {"title" : title, 'form' : form}
            return render(request, 'app/form.html', context = context)


def image_page(request):
    title = "Image Generator"
    if request.method =="POST" :
        # form.save()
        description = getDescription(request)
        image_url = gen.generateImage(description)
        context = {"title" : title, 'image_url' : image_url, 'description' : description}
        return render(request, 'app/image.html', context = context)
    else :
        form = forms.ApiForm()
        context = {"title" : title, 'form' : form}
        return render(request, 'app/form.html', context = context)


def code_page(request): 
        title = "Code Generator"
        if request.method =="POST" :
            # form.save()
            description = getDescription(request)
            code = gen.generateCode(description)
            context = {"title" : title, 'code' : code}
            return render(request, 'app/code.html', context = context)
        else :
            form = forms.ApiForm()
            context = {"title" : title, 'form' : form}
            return render(request, 'app/form.html', context = context)


@login_required
def profil_page(request) :
    title = "Espace Personnelle"
    context = {"title" : title}
    return render(request, 'registration/profil.html', context = context)


def contact_page(request):
    title = "Contact"
    context = {"title" : title}
    return render(request, 'app/contact.html', context = context)

    
def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('url_home')
        else:
            messages.info(request, "L'adresse email et le mot de passe ne correspondent pas !")
            

    context = {}
    return render(request, 'accounts/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')

class ModelListView(LoginRequiredMixin,ListView) :
    model = models.FormModel
    template_name = "app/List_request.html"
    context_object_name = "request_app"

class SignUpPage(CreateView) :
    form_class = forms.UserFormCustom
    success_url = reverse_lazy('login')
    template_name = "registration/signUp.html"
