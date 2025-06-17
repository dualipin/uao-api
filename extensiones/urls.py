from rest_framework.routers import DefaultRouter
from .views import ExtensionViewSet

router = DefaultRouter()
router.register(r"extensiones", ExtensionViewSet, basename="extension")

urlpatterns = router.urls
