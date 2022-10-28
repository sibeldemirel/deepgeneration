from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm

class ApiForm(forms.ModelForm):
    class Meta:
        model = models.ApiModel
        fields = "__all__"
        # labels = {
        #     "description": "Entrez une description ",
        # 
    
class UserFormCustom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = "__all__"
