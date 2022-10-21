from django.db import models


class ApiModel(models.Model):
    description = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )
