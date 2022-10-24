from django.shortcuts import render
from . import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from . import user, generator

import requests


user = user.User()
gen = generator.Generator(user)

def home_page(request):
    title = "Accueil"
    context = {"title" : title}
    return render(request, 'app/home.html', context = context)


def getDescription(request):
    form = forms.ApiForm(request.POST)
    if form.is_valid() :
        description = form.cleaned_data['description']
        return description

def article_page(request):
    title = "Blog Generator"
    blog = request.session['blog']
    context = {"blog" : blog, 'title' : title}
    return render(request, 'app/article.html', context = context)

def blog_page(request):
    title = "Blog Generator"
    if request.method =="POST" :
        # form.save()
        description = getDescription(request)
        blog = gen.generateBlog(description)
        request.session['blog'] = blog
        context = {"title" : title, 'blog' : blog}
        return render(request, 'app/blog.html', context = context)
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

    
