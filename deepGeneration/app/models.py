from django.db import models
import datetime


class ApiModel(models.Model):
    description = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )



class BlogModel(models.Model):

    title = models.CharField(
        max_length=500,
        blank=False,
        null=False,
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
    
    scrap_date = models.DateTimeField()

    url_image = models.URLField(
        max_length=500,
        blank=False,
        null=False,
    )