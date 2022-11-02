import nlpcloud

class Generator :

    stableModel = "stable-diffusion"
    fastModel = "fast-gpt-j"
    accuracyModel = "finetuned-gpt-neox-20b"


    def __init__(self, user) :
        self.__user  = user

    def getUser(self) :
        return self.__user

    def setModel(self, model) :
        self.__model = model

    def getModel(self) :
        return self.__model

    def getClient(self) :
        return nlpcloud.Client(self.getModel(), self.getUser().getToken(), True, lang=self.getUser().getUserLanguage())
        # return nlpcloud.Client(self.getModel(), self.getUser().getToken())

    def generateArticle(self, description) :
        self.setModel(Generator.fastModel)
        return self.getClient().article_generation(description)['generated_article']

    def generateCode(self, description) :
        self.setModel(Generator.accuracyModel)
        return self.getClient().code_generation(description)['generated_code']

    def generateImage(self, description) :
        self.setModel(Generator.stableModel)
        return self.getClient().image_generation(description)['url']

    def generateSummarization(self, description) :
        self.setModel(Generator.accuracyModel)
        return self.getClient().summarization(description)['summary_text']

    
