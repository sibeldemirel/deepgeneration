from django.shortcuts import render

import requests
import nlpcloud

class User :

    defaultToken = "f27c25c9364eb17c5fb56f5f9f27f44615f7f35a"
    defaultLanguage = 'en'

    def __init__(self, token=defaultToken) :
        self.__userLanguage = User.defaultLanguage
        self.__token = token

    def getUserLanguage(self) :
        return self.__userLanguage

    def setUserlanguage(self, newUserLanguage) :
         self.__userLanguage = newUserLanguage

    def getToken(self) :
        return self.__token


class Generator :

    stableModel = "stable-diffusion"
    fastModel = "fast-gpt-j"
    accuracyModel = "finetuned-gpt-neox-20b"


    def __init__(self, user) :
        self.__user : User = user

    def getUser(self) :
        return self.__user

    def setModel(self, model) :
        self.__model = model

    def getModel(self) :
        return self.__model

    def getClient(self) :
        return nlpcloud.Client(self.getModel(), self.getUser().getToken(), True, lang=self.getUser().getUserLanguage())

    def generateBlog(self, description) :
        self.setModel(Generator.fastModel)
        return self.getClient().article_generation(description)['generated_article']

    def generateCode(self, description) :
        self.setModel(Generator.accuracyModel)
        return self.getClient().code_generation(description)['generated_code']

    def generateImage(self, description) :
        self.setModel(Generator.stableModel)
        return self.getClient().image_generation(description)['url']

    
def countLeftSpace(s) :
    return (len(s) - len(s.lstrip()))

user = User()
gen = Generator(user)

def home_page(request):
    title = "Accueil"
    context = {"title" : title}
    return render(request, 'app/home.html', context = context)

def image_page(request):
    title = "Image Generator"
    image_url = gen.generateImage('a beautifull landscape')
    context = {"title" : title, 'image_url' : image_url}
    return render(request, 'app/image.html', context = context)

def code_page(request):
    title = "Code Generator"
    code = gen.generateCode('python recursive factorial program')
    context = {"title" : title, 'code' : code}
    return render(request, 'app/code.html', context = context)

def blog_page(request):
    title = "Blog Generator"
    blog = gen.generateBlog('how to become a programmer ?')
    context = {"title" : title, 'blog' : blog}
    return render(request, 'app/blog.html', context = context)