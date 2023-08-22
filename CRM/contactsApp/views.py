from django.shortcuts import render, redirect
from .models import Contact, Entite
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .forms import LoginForm
from django.contrib import messages
from .models import  UserProfile



# Create your views here.

def contacts(request):
    contacts = Contact.objects.all()
    return render(request, "contacts.html", context = {'contacts':contacts})

class ContactDetail (DetailView):
    model = Contact
    template_name = 'contact.html'

def contact (request):
    contact = Contact.objects.get(pk=1)
    return render(request, 'contact.html', context = {'contact':contact})

def contact_detail (request, pk):
    contact = Contact.objects.get(pk=pk)
    return render(request, 'contact.html', context = {'contact':contact})




def entites(request):
    entites = Entite.objects.all()
    return render(request, "entites.html", context = {'entites':entites})

class EntiteDetail(DetailView):
    model = Entite
    template_name= 'entite.html'

def entite(request):
    entite = Entite.objects.get(pk=1)
    return render(request, "entite.html",context = {'entite':entite})

def entite_detail(request,pk):
    entite = Entite.objects.get(pk=pk)
    return render(request, "entite.html",context = {'entite':entite})


def page_login (request):
    message = ''
    if request.method == 'POST':
        user = authenticate(
            username = request.POST['username'],
            password = request.POST['password'],
            )
        if user is not None : #s'il existe bien en base un couple username/password saisi au préalable, la fonction authenticate renvoie l'objet utilisateur correspond. Sinon, elle renvoie None
            login(request,user)
            messages.success (request,'Vous êtes connecté.' )
            return redirect ('contacts')
        else :
            message = 'Votre adresse mail ou votre mot de passe est erroné'
    return render(
        request,"login.html", context={'message':message}
    )

def register (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate( username = username, password = password)
            login (request, user)
            messages.success (request, 'Bonjour, votre compte a été crée avec succès')
            return redirect  ('contacts')
    else :
        form = UserCreationForm()
    return render (request,"register.html", context= {'form' : form } )


@login_required #l'utilisateur doit être connecté pour se déconnecter
def logout_user(request):
    logout(request)
    return redirect('login')



def page_profil (request):
    return render(request, 'profil.html')



def modification_profil(request):
    profil_utilisateur= request.user.username #profil personnalisé

    if request.method == 'POST':
        form = UserProfile(request.POST, request.FILES, instance=profil_utilisateur)
        if form.is_valid():
            form.save()
            return redirect('profil')
    else:
        form = UserProfile(instance=profil_utilisateur)

    return render(request, 'modification_profil.html', {'form': form})
