from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, Entite
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .forms import EditProfileForm, NewEntite
from django.contrib import messages
from .models import  UserProfile
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy





# Create your views here.

def contacts(request):
    if request.user.is_authenticated : 
        contacts = Contact.objects.all()
        return render(request, "contacts.html", context = {'contacts':contacts})
    else :
        return redirect('login')

class ContactDetail (DetailView):
    model = Contact
    template_name = 'contact.html'

def contact (request):
    if request.user.is_authenticated : 
        contact = Contact.objects.get(pk=1)
        return render(request, 'contact.html', context = {'contact':contact})
    else :
        return redirect('login')
    
def contact_detail (request, pk):
    if request.user.is_authenticated : 
        contact = Contact.objects.get(pk=pk)
        return render(request, 'contact.html', context = {'contact':contact})
    else :
        return redirect('login')


def entites(request):
    if request.user.is_authenticated : 
        entites = Entite.objects.all()
        return render(request, "entites.html", context = {'entites':entites})
    else :
        return redirect('login')

        

class EntiteDetail(DetailView):
    model = Entite
    template_name= 'entite.html'

def entite(request):
    if request.user.is_authenticated : 
        entite = Entite.objects.get(pk=1)
        return render(request, "entite.html",context = {'entite':entite})
    else :
        return redirect('login')

def entite_detail(request,pk):
    if request.user.is_authenticated : 
        entite = Entite.objects.get(pk=pk)
        return render(request, "entite.html",context = {'entite':entite})
    else :
        return redirect('login')

#ajouter une nouvelle entite
def add_entite(request):
    if request.user.is_authenticated : 
        if request.method == 'POST':
            form = NewEntite(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('entites')
        else :
            form = NewEntite()

        return render(request, 'entite_new.html', {'form': form})
    else :
        return redirect ('login')


#connection utilisateur
def page_login (request):
    form = AuthenticationForm(request, request.POST)
    if request.method == 'POST':
        user = authenticate(
            username = request.POST['username'],
            password = request.POST['password'],
            )
        if user is not None : #s'il existe bien en base un couple username/password saisi au préalable, la fonction authenticate renvoie l'objet utilisateur correspond. Sinon, elle renvoie None
            login(request,user)
            print(request)
            messages.success (request,'Vous êtes connecté.', extra_tags='success' )
            print(request)
            return redirect ('contacts')
        else :
            messages.error (request, 'Votre adresse mail ou votre mot de passe est erroné')
    return render(
        request,"login.html" ,   context= {'form' : form}  )

#création d'un compte utilisateur
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
    return render (request,"register.html", context= {'form' : form} )

#déconnection utilisateur
def logout_user(request):
    if request.user.is_authenticated : 
        logout(request)
        return redirect('login')
    else :
        redirect('login')


#visualisation du profil utilisateur
def view_profile (request):
    if request.user.is_authenticated : 
        user_profile = UserProfile.objects.get(user=request.user)
        return render(request, 'view_profile.html', {'user_profile': user_profile})
    else :
        redirect('login')

#modification du profil utilisateur
def edit_profile(request):
    if request.user.is_authenticated : 
        
        user_profile = UserProfile.objects.get(user=request.user)
        #user_form = CustomUserChangeForm(request.POST or None,instance=request.user) #pour changer les éléments qui appartiennent à la classe User (nom, prénom etc)
        #profile_form = EditProfileForm(request.POST or None, instance=user_profile) #pour changer les autres éléments de UserProfil (date de naissance, image etc)

        if request.method == 'POST':
            #user_form = CustomUserChangeForm(request.POST, instance=request.user) #pour changer les éléments qui appartiennent à la classe User (nom, prénom etc)
            profile_form = EditProfileForm(request.POST, request.FILES, instance=user_profile) #pour changer les autres éléments de UserProfil (date de naissance, image etc)

            if profile_form.is_valid() :
                #user_form.save()
                profile_form.save()
                return redirect('profile')
        #print(user_form)
        user_profile = UserProfile.objects.get(user=request.user)
        profile_form = EditProfileForm(instance=user_profile)
        
        return render(request, 'edit_profile.html',{ 'profile_form': profile_form})
    
    else :
        redirect('login')


#modification du mot de passe quand le user est connecté
def change_password(request, user_id):
    if request.user.is_authenticated : 
        user = get_object_or_404(UserProfile, id=user_id)
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user) #mettre à jour l'auth de l'utilisateur pour qu'il reste connecté après modification du mdp
                messages.success(request, 'Votre mot de passe a été mis à jour avec succès.')
                return redirect('view_profil')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {'form': form})
    
    else :
        redirect('login')

#test modification du mot de passe quand le user est connecté
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'  
    success_url = reverse_lazy('change_password')


#repartition des sources d'acquisition

def repartition_source_acquisition(request):
    contacts = Contact.objects.all() #on récupère tous les contacts
    comptabilite = {}
    repartition = {}
    nbre_sources = 0
    for contact in contacts :
        source_acquisition = contact.source_acquisition
        comptabilite[source_acquisition] = comptabilite.get(source_acquisition, 0) + 1
        nbre_sources +=1
        print(nbre_sources)
    
    for elem in comptabilite.keys() :
            if nbre_sources > 0 :
                repartition[elem]=comptabilite[elem]/nbre_sources*100
            else :  
                repartition[elem] = 0
    return render(request, 'acquisition_source.html', {'repartition': repartition})