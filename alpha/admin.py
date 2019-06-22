from django.contrib import admin
from .models import Editor

# Registered models here.


class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('Editor',)

admin.site.register(Editor)

