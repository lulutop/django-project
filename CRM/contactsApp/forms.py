from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile


#class UserForm (UserCreationForm):
#    class Meta :
#        model = User
#        fields = [ 'username',
#                   'password1' ,
#                   'password2', 
#                   'email']


#class LoginForm(forms.AuthentificationForm):
#    username = forms.CharField(max_length=64, label = 'Identifiant')
#    password = forms.CharField(max_length=64, widget=forms.PasswordInput, label = 'Mot de passe')

#On hérite de la classe UserChangeForm et on spécifie les champs qu'on soiuhaite inclure dans le formulaire
#certains champs du formulaire de la classe UserChangeForm sont obligatoires mais on ne souhaite pas les mettre à jour
class CustomUserChangeForm(UserChangeForm):
    class Meta :
        model = User
        fields = ['first_name','last_name']

#On crée une seconde classe pour pouvoir mettre à jour des champs qui ne sont pas inclus dans UserChangeForm
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [ 'birth_date', 'image']

