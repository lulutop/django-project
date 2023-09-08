from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms




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
    CHOICES = [('Linkedin','Linkedin'),('Reco','Recommandation'),('RDV tel','RDV télephonique') ]
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
    type_prive = models.BooleanField(null=True)
    source_acquisition = models.CharField(max_length=128, choices = CHOICES, null=True)
    commentaire = models.CharField(max_length=244, null=True)

  
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
 #   first_name = models.CharField(max_length=50, null=True)
 #   last_name = models.CharField(max_length=50, null=True)
    birth_date = models.DateField(null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)

#à la création d'un nouvel utilisateur, un profil rattaché va être créé
@receiver(post_save, sender=User)
def createProfile(sender, instance, created,**kwargs):
    if created :
        UserProfile.objects.create(user=instance)






    
