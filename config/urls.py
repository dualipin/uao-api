"""
URL configuration for config project.
It exposes the URL patterns for the Django project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_patterns = [
    path("", include("usuarios.urls")),
    path("", include("extensiones.urls")),
    path("", include("carreras.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(app_patterns), name="app_urls"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
