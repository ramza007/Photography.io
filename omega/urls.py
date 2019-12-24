"""
omega URL Configuration

"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from alpha import views

handler404 = views.error_404
handler500 = views.error_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alpha.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
