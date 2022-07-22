"""
App urls
"""
# from django.conf.urls import url, handler404, handler500
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('photography', views.photos, name='photos'),
    path('email', views.email, name='email'),
    path('thank-you', views.thankyou, name='thankyou'),
    path('landscapes', views.landscapes, name='landscapes'),
    path('architecture', views.architecture, name='architecture'),
]
