from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm

class ApiForm(forms.ModelForm):
    class Meta:
        model = models.FormModel
        fields = "__all__"
    
class UserFormCustom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = "__all__"