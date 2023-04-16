"""
App urls
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('photography', views.photos, name='photos'),
    path('email', views.email, name='email'),
    path('thank-you', views.thankyou, name='thankyou'),
    path('landscapes', views.landscapes, name='landscapes'),
    path('architecture', views.architecture, name='architecture'),
    path('automobiles', views.automobiles, name='automobiles'),
]

# Serving static files during development only
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
