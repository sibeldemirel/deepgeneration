from django import forms
from . import models


class ApiForm(forms.ModelForm):
    class Meta:
        model = models.ApiModel
        fields = "__all__"
        labels = {
            "description ": " entrez votre description",
        }