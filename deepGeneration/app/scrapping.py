from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys
import time
import requests
from generator import Generator
from user import User



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

def generateArticles(url):
    html = getHtml(url)
    themesList = getThemes(html)
    articles = []
    # return [gen.generateArticle(theme) for theme in themesList]
    for theme in themesList :
        try :
            article = gen.generateArticle(theme)
            articles.append(article)
        except requests.exceptions.HTTPError :
            erreur = sys.exc_info()
            msgerr = u"%s" % (erreur[1])
            codeErreur = msgerr.split(' ')[0]
            if (codeErreur == '400') :
                theme = gen.generateSummarization(theme)
            elif (codeErreur == '429') :
                time.sleep(60)
            else :
                break
    return articles



def generateArticles(url):
    html = getHtml(url)
    themesList = getThemes(html)
    articles = []
    idx_theme = 0
    # return [gen.generateArticle(theme) for theme in themesList]
    while idx_theme < len(themesList):
        try :
            article = gen.generateArticle(themesList[idx_theme])
            articles.append(article)
            idx_theme+=1
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




if __name__ == '__main__':
    url = NYTurl
    articles = generateArticles(url)
    