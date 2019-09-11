from django.contrib import admin
from .models import Location, Timeshot, Details, Image, NewsletterRecepients

# Registered models here.

admin.site.register(Location)
admin.site.register(Timeshot)
admin.site.register(Details)
admin.site.register(Image)
admin.site.register(NewsletterRecepients)