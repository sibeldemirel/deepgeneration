from django.shortcuts import render

def home_page(request):
    title = "Accueil"
    context = {"title" : title}
    return render(request, 'app/home.html', context = context)

def image_page(request):
    title = "Image Generator"
    context = {"title" : title}
    return render(request, 'app/image.html', context = context)

def blog_page(request):
    title = "Blog Generator"
    context = {"title" : title}
    return render(request, 'app/blog.html', context = context)

def code_page(request):
    title = "Code Generator"
    context = {"title" : title}
    return render(request, 'app/code.html', context = context)

