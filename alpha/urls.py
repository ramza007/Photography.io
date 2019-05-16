from django.conf.urls import url
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('photography', views.photos, name='photos'),
]