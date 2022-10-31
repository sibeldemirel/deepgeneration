import string
import os
from dotenv import load_dotenv
load_dotenv()
# TOKEN = os.getenv("TOKEN")
TOKEN = "f27c25c9364eb17c5fb56f5f9f27f44615f7f35a"
# from django.contrib.auth.models import User

# User.Object.create_user('john','ttt','ttt')

class User :

    defaultToken = TOKEN
    defaultLanguage = 'en'

    def __init__(self, token=defaultToken) :
        self.__userLanguage = User.defaultLanguage
        self.__token = TOKEN
        self.__imgs_url = [string]
        self.__codes = [string]
        self.__articles = [string]

    def getUserLanguage(self) :
        return self.__userLanguage

    def setUserlanguage(self, newUserLanguage) :
         self.__userLanguage = newUserLanguage

    def getToken(self) :
        return self.__token

    def getImgUrl(self) :
        return self.__imgs_url

    def addImgUrl(self,last_url) :
        self.__imgs_url.append(last_url)

    def deleteImgUrl(self, url):
        self.__imgs_url.pop(url)

    def getCodes(self) :
        return self.__codes

    def addCode(self,last_code) :
        self.__codes.append(last_code)

    def deleteCode(self, code):
        self.__codes.pop(code)

    def getArticles(self) :
        return self.__articles

    def addArticle(self,last_articles) :
        self.__articles.append(last_articles)

    def deleteArticle(self, articles):
        self.__articles.pop(articles)

