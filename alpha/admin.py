from django.contrib import admin
from .models import Location, Timeshot, Details, Image

# Registered models here.

admin.site.register(Location)
admin.site.register(Timeshot)
admin.site.register(Details)
admin.site.register(Image)
