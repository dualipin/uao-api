from django.urls import path
from .views import PerfilView, UsuarioViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("usuarios", UsuarioViewSet, basename="usuarios")

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify", TokenVerifyView.as_view(), name="token_verify"),
    path("perfil/", PerfilView.as_view(), name="perfil"),
] + router.urls
