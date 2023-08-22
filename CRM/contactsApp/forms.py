from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm (UserCreationForm):
    class Meta :
        model = User
        fields = [ 'username',
                   'password1' ,
                   'password2', 
                   'email']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=64, label = 'Identifiant')
    password = forms.CharField(max_length=64, widget=forms.PasswordInput, label = 'Mot de passe')


class ModificationProfil(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']

test = True
