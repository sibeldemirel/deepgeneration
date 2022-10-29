from django.core.management.base import BaseCommand, CommandError
# from ...models import BlogModel
# from . import scrapping

# from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys
import time
import requests
from datetime import date
from .generator import Generator
from .user import User
from ...models import BlogModel


getTexts = lambda l : [b.getText(strip = True) for b in l]

NYTurl = "https://www.nytimes.com/section/world"
CNNurl = "https://edition.cnn.com/world"

user = User()
gen = Generator(user)


def getHtml(url) :
    page = requests.get(url)
    if not page.ok :
        raise Exception('Failed to load page {}'.format(page.status_code))
    html = BeautifulSoup(page.text, 'html.parser')  
    return html

def getThemes(html) :
    brutList = html.find_all('p', class_ = "css-1pga48a e15t083i1")
    themesList = getTexts(brutList)
    return themesList

def getDates(html) :
    brutList = html.find_all('div', class_="css-agsgss e15t083i3")
    datesList = getTexts(brutList)
    return datesList

list_month = [
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec'
]

tuple_list_month = [((list_month[idx_m],idx_m+1)) for idx_m in range(len(list_month))]
dict_month = dict(tuple_list_month)

def modifyDate(scrap_date) :
    split1 = scrap_date.replace(' ','').split(".")
    str_month = split1[0]
    month = dict_month[str_month]
    split2 = split1[1].split(',')
    day = int(split2[0])
    year = int(split2[1])
    article_date = date(year,month,day)
    return article_date

def getDates(html) :
    datesList = []
    brutList = html.find_all('div', class_="css-agsgss")
    for div in brutList :
        print(div)
        # scrap_date = div.span.getText(strip = True)
        # article_date = modifyDate(scrap_date)
        # datesList.append(article_date)
    return datesList

    



# def generateArticles(url):
#     html = getHtml(url)
#     themesList = getThemes(html)
#     # datesList = getDates(html)
#     articles = []
#     idx_theme = 0
#     blog = BlogModel()
#     while idx_theme < len(themesList):
#         try :
#             article = gen.generateArticle(themesList[idx_theme])
#             articles.append(article)
#             idx_theme+=1
#             blog.description = themesList[idx_theme]
#             # blog.article_date = datesList[idx_theme]
#             blog.article = article
#             blog.scrap_date = date.today()
#             blog.save()
#             print("idx_theme")
#         except requests.exceptions.HTTPError :
#             erreur = sys.exc_info()
#             msgerr = u"%s" % (erreur[1])
#             codeErreur = msgerr.split(' ')[0]
#             if (codeErreur == '400') :
#                 print('400')
#                 themesList[idx_theme] = gen.generateSummarization(themesList[idx_theme])
#             elif (codeErreur == '429') :
#                 print('429')
#                 time.sleep(20)
#     return articles


def generateArticles(url):
    html = getHtml(url)
    themesList = getThemes(html)
    # datesList = getDates(html)
    articles = []
    idx_theme = 0
    while idx_theme < len(themesList):
        try :
            article = gen.generateArticle(themesList[idx_theme])
            articles.append(article)
            idx_theme+=1
            blog = BlogModel(description = themesList[idx_theme],article = article, article_date = date.today())
            blog.save()
            # blog.article_date = datesList[idx_theme]
            print("idx_theme")
        except requests.exceptions.HTTPError :
            erreur = sys.exc_info()
            msgerr = u"%s" % (erreur[1])
            codeErreur = msgerr.split(' ')[0]
            if (codeErreur == '400') :
                print('400')
                themesList[idx_theme] = gen.generateSummarization(themesList[idx_theme])
            elif (codeErreur == '429') :
                print('429')
                time.sleep(20)
    return articles


class Command(BaseCommand):
    help = 'Does some magical work'

    def handle(self, *args, **options):
        """ Do your work here """
        generateArticles(NYTurl)
        self.stdout.write('There are {} things!'.format(BlogModel.objects.count()))