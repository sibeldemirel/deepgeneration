from django import forms

from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class ApiForm(forms.ModelForm):
    class Meta:
        model = models.ApiModel
        fields = "__all__"
    
# class UserFormCustom(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         fields = "__all__"


class CreateUserForm(UserCreationForm):
    # email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder':'Nom..'})
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Email..'})
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Mot de passe..'})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Confirmer mot de passe..'})


    # def save(self, commit=True):
    #     user = super(CreateUserForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user
