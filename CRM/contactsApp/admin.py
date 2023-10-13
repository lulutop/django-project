from django.contrib import admin
from .models import Contact, Entite, SourceAcquisition

# Register your models here.
admin.site.register(Contact)
admin.site.register(Entite)
admin.site.register(SourceAcquisition)