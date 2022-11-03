from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import sys
import time
import requests
from .generator import Generator
from .user import User
from ...models import ImageModel, ArticleModel
# from django.utils import timezone
# from . import scrapping


getTexts = lambda l : [b.getText(strip = True) for b in l]

NYTurl = "https://www.nytimes.com/section/world"
CNNurl = "https://edition.cnn.com/world"

user = User()
gen = Generator(user)


def getHtml(url):
    page = requests.get(url)
    if not page.ok :
        raise Exception('Failed to load page {}'.format(page.status_code))
    html = BeautifulSoup(page.text, 'html.parser')  
    return html

def getTitles(html):
    brutList = html.find_all('h2', class_ = "css-14g652u e1y0a3kv0")
    titlesList = getTexts(brutList)
    return titlesList

def getDescription(html) :
    brutList = html.find_all('p', class_ = "css-1pga48a e15t083i1")
    descriptionsList = getTexts(brutList)
    return descriptionsList

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
        # article_date = div.span.getText(strip = True)
        # article_date = modifyDate(article_date)
        # datesList.append(article_date)
    return datesList



def generateArticles(url):
    html = getHtml(url)
    descriptionsList = getDescription(html)
    titlesList = getTitles(html)
    idx_theme = 0
    a=0
    while idx_theme < len(descriptionsList):
        try :
            if a==0:
                article = gen.generateArticle(descriptionsList[idx_theme])
                a=1
                url_image = gen.generateImage(descriptionsList[idx_theme])
                a=0
            else:
                image = gen.generateImage(descriptionsList[idx_theme])
                a=0
            
        except requests.exceptions.HTTPError :
            erreur = sys.exc_info()
            msgerr = u"%s" % (erreur[1])
            codeErreur = msgerr.split(' ')[0]
            if (codeErreur == '400') :
                print('400')
                descriptionsList[idx_theme] = gen.generateSummarization(descriptionsList[idx_theme])
            elif (codeErreur == '429') :
                print('429')
                time.sleep(20)
        else :
            idx_theme+=1
            article += '\n <img src="'+ url_image +'">'
            article= ArticleModel(title=titlesList[idx_theme],description=descriptionsList[idx_theme],article=article)#, generating_date=today)
            image= ImageModel(description=descriptionsList[idx_theme],url_image=url_image)#,generating_date=today)
            article.save()
            image.save()
            print(idx_theme)


class Command(BaseCommand):
    help = 'Does some magical work'

    def handle(self, *args, **options):
        """ Do your work here """
        generateArticles(NYTurl)
        self.stdout.write('There are {} things!'.format(ArticleModel.objects.count()))