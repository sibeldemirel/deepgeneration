from django.db import models


class ApiModel(models.Model):
    description = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )


class BlogModel(models.Model):
    description = models.TextField(
        # max_length=500,
        blank=False,
        null=False,
    )
    contenu = models.TextField(
        # max_length=500,
        blank=False,
        null=False,
    )
    # date = 


