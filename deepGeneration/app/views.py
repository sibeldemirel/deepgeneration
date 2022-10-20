from django.shortcuts import render

def home_page(request):
    title = "Accueil"
    context = {"title" : title}
    return render(request, 'app/home.html', context = context)

def image_page(request):
    title = "Image Generator"
    context = {"title" : title}
    return render(request, 'app/imageG.html', context = context)