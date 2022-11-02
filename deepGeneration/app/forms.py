from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm

class ApiForm(forms.ModelForm):
    class Meta:
        model = models.FormModel
        fields = "__all__"
    
class UserFormCustom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(UserFormCustom, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder':'Nom..'})
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Email..'})
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Mot de passe..'})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Confirmer mot de passe..'})