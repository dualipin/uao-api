from .views import CarreraViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r"carreras", CarreraViewSet, basename="carrera")

urlpatterns = router.urls