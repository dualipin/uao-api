from rest_framework.routers import DefaultRouter
from .views import CarreraViewSet

router = DefaultRouter()

router.register(r"carreras", CarreraViewSet, basename="carrera")

urlpatterns = router.urls
