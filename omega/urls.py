"""
omega URL Configuration

"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from alpha import urls, views
# from django.conf.urls import url
from django.views.static import serve
from alpha import views as alpha_views

handler404 = views.error_404
handler500 = views.error_500
handler404 = alpha_views.error_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alpha.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

# urls(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

# if settings.DEBUG:
#     urlpatterns += [
#         url(r'^media/(?P<path>.*)$', serve, {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#     ]
