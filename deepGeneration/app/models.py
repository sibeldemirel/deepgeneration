from django.db import models


class FormModel(models.Model):
    description = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )



class ArticleModel(models.Model):

    title = models.CharField(
        max_length=500,
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=False,
        null=False,
    )

    article = models.TextField(
        blank=False,
        null=False,
    )

    # article_date = models.DateTimeField()
    
    generating_date = models.DateTimeField()



class ImageModel(models.Model):

    description = models.TextField(
    blank=False,
    null=False,
    )

    url_image = models.URLField(
    max_length=500,
    blank=False,
    null=False,
    )

    generating_date = models.DateTimeField()


class CodeModel(models.Model):

    description = models.TextField(
    blank=False,
    null=False,
    )

    code = models.TextField(
    blank=False,
    null=False,
    )

    generating_date = models.DateTimeField()