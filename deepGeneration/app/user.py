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