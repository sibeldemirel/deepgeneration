from django import forms

from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ApiForm(forms.ModelForm):
    class Meta:
        model = models.ApiModel
        fields = "__all__"
    
class UserFormCustom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = "__all__"


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
