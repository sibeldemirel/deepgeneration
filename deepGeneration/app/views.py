from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
# from . import user, generator, forms, models
from .management.commands import generator, user
# from .forms import UserFormCustom


from os import getenv
import requests
# from .secret import token


from . import forms, models

user = user.User()
gen = generator.Generator(user)

def home_page(request):
    title = "Accueil"
    context = {"title" : title}
    return render(request, 'app/home.html', context = context)


def getDescription(form):
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
    form = forms.ArticleForm(request.POST or None)
    if request.method =="POST" :
        articleForm = form.save(commit=False)
        articleForm.user = request.user
        
        description = getDescription(form)   
        article = gen.generateArticle(description)
        articleForm.article = article
        articleForm.save()
        context = {"title" : title, 'article' : article}
        request.session['article'] = article
        request.session['title'] = title
        return render(request, 'app/code_article.html', context = context)
    else :
            context = {"title" : title, 'form' : form}
            return render(request, 'app/form.html', context = context)


def image_page(request):
    title = "Image Generator"
    form = forms.ImageForm(request.POST or None)
    if request.method =="POST" :
        imageForm = form.save(commit=False)
        imageForm.user = request.user
        description = getDescription(form)
        image_url = gen.generateImage(description)
        imageForm.url_image = image_url
        imageForm.save()
        context = {"title" : title, 'image_url' : image_url, 'description' : description}
        return render(request, 'app/image.html', context = context)
    else :
        context = {"title" : title, 'form' : form}
        return render(request, 'app/form.html', context = context)


def code_page(request): 
        title = "Code Generator"
        form = forms.CodeForm(request.POST or None)
        if request.method =="POST" :
            codeForm = form.save(commit=False)
            codeForm.user = request.user
            description = getDescription(form)
            code = gen.generateCode(description)
            codeForm.code = code
            codeForm.save()
            context = {"title" : title, 'code' : code}
            return render(request, 'app/code.html', context = context)
        else :
            context = {"title" : title, 'form' : form}
            return render(request, 'app/form.html', context = context)


@login_required
def profil_page(request) :
    user_id = request.user.id
    articles = models.ArticleModel.objects.all().filter(user_id= user_id)
    images = models.ImageModel.objects.all().filter(user_id= user_id)
    codes = models.CodeModel.objects.all().filter(user_id= user_id)
    title = "Historique"
    context = {"title" : title, 'articles' : articles, 'images' : images, 'codes' : codes}
    return render(request, 'registration/profil.html', context = context,)


def contact_page(request):
    title = "Contact"
    context = {"title" : title}
    return render(request, 'app/contact.html', context = context)


def logout_page(request):
    logout(request)
    return redirect('login')


class SignUpPage(CreateView) :

    def get_context_data(self, **kwargs):
        title = 'Inscription'
        context = super().get_context_data(**kwargs)
        context['title'] = title
        # messages.success(request, 'Votre compte a été crée avec succès !')
        return context

    form_class = forms.UserFormCustom
    success_url = reverse_lazy('login')
    template_name = "registration/signUp.html"


def imageDetail_page(request,id):
    title = "Image Generator"
    image = get_object_or_404(models.ImageModel,pk=id)
    context = {"title" : title, 'image_url' : image.url_image, 'description' : image.description}
    return render (request,'app/image.html',context=context)


def articleDetail_page(request,id):
    title = "Article Generator"
    article = get_object_or_404(models.ArticleModel,pk=id)
    context = {"title" : title, 'article' : article.article}
    return render (request,'app/code_article.html',context=context)

def codeDetail_page(request,id):
    title = "Code Generator "
    code = get_object_or_404(models.CodeModel,pk=id)
    context = {"title" : title, 'code' : code.code}
    return render (request,'app/code.html',context=context)


def articles_recent(request) :
    title = "Blog"
    all_articles = models.ArticleModel.objects.filter(user_id__isnull=True)
    # last_date = all_articles.values_list('generating_date').order_by('-generating_date')[4][0]
    # articles = all_articles.filter(generating_date=last_date)
    articles = all_articles.order_by('-generating_date')[:10]
    context = {"title" : title, "articles" : articles}
    return render(request, 'app/recent_articles.html', context = context)

def blogDetail_page(request,id):
    title = "Article"
    article = get_object_or_404(models.ArticleModel,pk=id)
    request.session['title'] = title 
    request.session['article'] = article.article
    context = {"title" : title, 'article' : article.article}
    return render (request,'app/code_article.html',context=context)
