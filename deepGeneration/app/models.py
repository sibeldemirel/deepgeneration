from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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
    
    generating_date = models.DateTimeField(
        default=timezone.now,
        blank=False,
        null=False,
    )

    user = models.ForeignKey(User,
    null=True,
    blank=True,
    on_delete=models.CASCADE,
    )


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

    generating_date = models.DateTimeField(
        default=timezone.now,
        blank=False,
        null=False,
        )

    user = models.ForeignKey(
    User,
    null=True,
    blank=True,
    on_delete=models.CASCADE,
    )


class CodeModel(models.Model):

    description = models.TextField(
    blank=False,
    null=False,
    )

    code = models.TextField(
    blank=False,
    null=False,
    )

    generating_date = models.DateTimeField(
        default=timezone.now,
        blank=False,
        null=False,)

    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        )
