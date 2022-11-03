from django import forms

from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

# class ApiForm(forms.ModelForm):
#     class Meta:
#         model = models.FormModel
#         fields = "__all__"

class ImageForm(forms.ModelForm):
    class Meta:
        model = models.ImageModel
        fields = ['description']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.ArticleModel
        fields = ['description']

class CodeForm(forms.ModelForm):
    class Meta:
        model = models.CodeModel
        fields = ['description']
    

class UserFormCustom(UserCreationForm):
    # email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(UserFormCustom, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder':'Nom..'})
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Email..'})
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Mot de passe..'})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Confirmer mot de passe..'})
