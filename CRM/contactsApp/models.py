from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save



# Create your models here.

class Entite(models.Model):
    nom = models.CharField(max_length = 128)
    logo = models.ImageField(upload_to='images', blank=True,  null=True)
    numero = models.IntegerField()
    adresse = models.CharField(max_length=128)
    code_postal = models.IntegerField()
    ville = models.CharField(max_length=128)
       
    def __str__(self):
        return "{}-{}".format(self.nom, self.adresse)
    
    def get_absolute_url(self):
        return reverse('entite-detail', kwargs ={'pk' : self.pk})
   
class Contact(models.Model):
    nom = models.CharField(max_length = 128)
    prenom = models.CharField(max_length=128)
    mail = models.EmailField(max_length=128)
    role = models.CharField(max_length = 128)
    #entreprise = models.CharField(max_length = 128)
    entite = models.ForeignKey(
        Entite, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name="contact")
    image = models.ImageField(upload_to='images', blank=True, null=True)
    type_privé = models.BooleanField()
    commentaire = models.CharField(max_length=244)

  
    def __str__(self):
        return "{} - {}".format(self.nom, self.prenom)
    
    def get_absolute_url(self):
        return reverse('contact-detail', kwargs = {'pk' : self.pk})
    
#class User (models.Model):
#  username = models.CharField(max_length=64)
#  password = models.CharField(max_length=64)
#  email = models.EmailField(max_length=64)
 # first_name = models.CharField(max_length=64)
 # last_name = models.CharField(max_length=64)

class UserProfile(models.Model): #Creation du profil
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=True, null=True)

def create_user_profile(sender, instance, created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)




    
