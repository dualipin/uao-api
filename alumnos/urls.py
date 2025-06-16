from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AlumnoViewSet, CartaBienvenidaView

router = DefaultRouter()

router.register(
    r"alumnos",
    AlumnoViewSet,
    basename="alumno",
)

urlpatterns = [
    path("alumnos/<int:pk>/carta-bienvenida/", CartaBienvenidaView.as_view(), name="carta-bienvenida"),
] + router.urls

