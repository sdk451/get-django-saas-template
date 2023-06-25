
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include, static
from django.conf import settings

from .routes import router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    url(r'^', include('cms.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('emails/', include('emails.urls', namespace='emails')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),

] + static.static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
