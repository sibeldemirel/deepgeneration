import email
from django.contrib import messages
from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from . import user, generator, forms, models
from .forms import CreateUserForm

# from

from os import getenv
import requests
# from .secret import token


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
    context = {'blog' : blog, 'title' : title}
    return render(request, 'app/article.html', context = context)

def blog_page(request):
    title = "Blog Generator"
    if request.method =="POST" :
        # form.save()
        description = getDescription(request)

        blog = """
        <h1>car</h1>
<p>The automobile has changed our lives, allowing us to travel anywhere and connect with friends and family half-way around the world. Car companies have responded to this demand by creating a variety of hybrid and electric vehicles specifically designed to make our lives easier. While some of these cars are luxurious and cost thousands of dollars, others are designed to get us from point A to point B as fast and affordably as possible. Here are some interesting facts about the car:</p>
<h2>The Car Is Older Than You Think</h2>
<p>If you think that cars were invented within the past century, then you're mistaken. Henry Ford built the first full-size car in 1896, and it was initially called the Quadra Motorcycle. The Model T Ford was introduced in 1908 and it changed the world. Since then, the automobile has evolved into something completely different, incorporating technology from aircraft and space travel.</p>
<p>Even today, over a hundred years later, cars are still evolving, implementing new technologies and changing the way we live.</p>
<h2>Most People Don't Know How To Maintain A Car</h2>
<p>If you own or have ever driven a car, then you'll know exactly what I'm talking about when I say that cars are complicated pieces of machinery that require a special knowledge to maintain properly. In addition to regular oil changes and tune-ups, cars require specialized tools, wiring, and know-how to work on them. Despite this, most people consider cars to be a quick and easy way to transport themselves and their possessions, which can often be the case when you're driving on a main street (assuming no accidents or traffic jams), but there is still a lot that goes into keeping a car running smoothly.</p>
<h2>Did You Know That Cars Were Originally Made Out Of Meat Tenderizers?</h2>
<p>Did you know that the first cars were actually made out of meat tenderizers? This is a fact that you will learn as you're driving around an auto-related encyclopedia in American History – The Definitive Collection. The first cars were initially built out of tin and wood, and their bodies were constructed out of hemp, animal bladders, and sometimes actual human flesh. They were fueled by alcohol, coal gas, or kerosene, and the drivers wore silk underwear and leather gloves. It wasn't until the early 20th century that cars were made out of more durable materials like steel and stainless steel.</p>
<h2>Most Cars Have Memories</h2>
<p>Did you know that the German car maker NSU introduced a vehicle with an onboard computer that analyzed driving patterns and remembered the past vehicles that each individual driver had owned? This feature is now found in all new cars and is commonly known as “Car-Friedrich”, named after the German designer who engineered the feature. Each time a car is started, its computer will scan a code that's been previously entered in and load the last five to seven kilometers of driving into the car's computer. This makes Car-Friedrich a smarter and safer vehicle, able to avoid collisions and improve gas mileage by anticipating what the driver wants and needs while on the road. It also helps reduce emissions and improve air quality by preventing cars from being driven with their doors open, reducing fuel consumption by as much as four percent.</p>
<h2>Hybrids Aren't Just For Future Fuel Economy Legislation</h2>
<p>Did you know that most automakers produce both gasoline- and electric-powered vehicles because there are times when a gasoline-only vehicle just won't do? There are certain tasks that you need a gas engine for, like climbing a mountain or hitting 60 mph. However, for most people who drive a car, gasoline hybrid engines make up a minority of their fleet. The majority of cars on the road today are powered by electric motors that run on stored energy. These electric motors are fueled by batteries, which are charged up when the engine is turned on and then stored when the ignition is off. This is why most cars now come with a plug that goes directly into the wall, allowing you to charge up while driving.</p>
<p>The combination of a gas engine with an electric motor allows automakers to offer vehicles that can get you where you need to go with the efficiency and power of an electric motor without having to rely on fossil fuels like gasoline or diesel. This is why automakers like Toyota, Honda, and Chevrolet produce both gas- and electric-powered vehicles. While gasoline-only vehicles still exist in some form, in others, such as the Toyota Prius and the Honda Civic, hybrid vehicles have rendered them obsolete.</p>
<h2>Electric Vehicles Will Soon Take Over</h2>
<p>Although electric vehicles are more expensive to buy and maintain, they have the advantage of being eco-friendly and reduce air pollution as well. Did you know that the use of electric vehicles has grown by 60% in the last five years and that the demand for them is predicted to double within the next five years? In fact, over 20 million electric vehicles will be on the road by the year 2030. This makes them a popular choice among people who want to reduce their ecological footprint and improve air quality – both of which are causing concern these days due to the rapidly increasing temperatures throughout the world.</p>
<h2>What Kind Of Insurance Do You Need To Own A Car?</h2>
<p>Did you know that the minimum liability insurance required for a car is three million dollars? This is because cars can and do get damaged on the roads every day, and the insurance companies are required to pay out to restore the vehicle to its pre-accident condition. This means that even if you have the best driver's insurance policy in the world, it won't matter if you have been in an accident if you don't have the money to repair your car. You will lose a lot of potential customers if you don't have a way for them to know you'll be able to fix their car once they've paid you back the cost of the repairs.</p>
<h2>Where Do You Park Your Car?</h2>
<p>Did you know that most Americans store their cars in the garage or on the street? According to a study from the American Automobile Association (AAA) as well as the Insurance Institute for Highway Safety (IIHS), most cars are parked on the street. This is largely because it's the most convenient place for people who want to drive and park on a whim. In addition to this, many garages are located in the neighborhood, which makes it easier for people to go for a walk or have a cup of coffee with a neighbor while their car is getting fixed.</p>
<p>On a related note, did you know that the average American spends over four hours a day in their car? According to a study from the AAA and the IIHS, drivers spend four hours a day in their cars, on average. This means that they're spending more time in their cars than they are at work or school. In the same way that kids grow up wanting to be doctors or lawyers, so too do many of today's car drivers wish to be mechanics or electricians once they've grown up.</p>
<h2>How Much Does It Cost To Maintain A Car?</h2>
<p>Did you know that the average cost of maintaining a car is about $500 per year? This is because cars require regular oil changes, tire rotations, and regular cleaning to maintain their cleanliness. These costs vary by manufacturer and model, but in general, they fall into the range of $100 to $400 per year. In terms of the bigger picture, owning a car is considered to be an investment, since you'll need to make a down payment and pay for gas and maintenance on a regular basis. When you consider the possible return on investment, it's clear that owning a car is a worthwhile endeavor for most people.</p>
<p>Curious about the car and its history? Want to find out more about the automobile and its place in society today? This informational encyclopedia will teach you everything you need to know about the car, from its inception to the modern day.</p> 
        """

        # blog = gen.generateBlog(description)
        # request.session['blog'] = blog
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

            code = """
            avec appel récursif

n = int(input("entrer un entier"))

def factoriel(n):
    if(n>1):
        return n*factoriel(n-1)
    elif(n==1):
        return 1
print(factoriel(n))
            """
            # code = gen.generateCode(description)
            context = {"title" : title, 'code' : code}
            return render(request, 'app/code.html', context = context)
        else :
            form = forms.ApiForm()
            context = {"title" : title, 'form' : form}
            return render(request, 'app/form.html', context = context)

def contact_page(request):
    title = "Contact"
    context = {"title" : title}
    return render(request, 'app/contact.html', context = context)

@login_required
def special_page(request) :
    title = "special"
    context = {"title" : title}
    return render(request, 'app/special_page.html', context = context)


class ModelListView(LoginRequiredMixin,ListView) :
    model = models.ApiModel
    template_name = "app/List_request.html"
    context_object_name = "request_app"

# def signup_page(request):
#     form = CreateUserForm()

#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=True)
#             messages.success(request, "Registration successful." )
#             return redirect("url_home")
#         messages.error(request, "Unsuccessful registration. Invalid information.")
#     form = CreateUserForm()
#     return render (request=request, template_name="registration/signup.html", context={'form':form})

def signup_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a été crée avec succès !')
            
            return redirect('login')
            
    context = {'form':form}
    return render (request=request, template_name="registration/signup.html", context=context)

   

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




