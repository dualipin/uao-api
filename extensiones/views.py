from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from shared.permissions import SoloListar
from .serializers import ExtensionSerializer
from .models import Extension


class ExtensionViewSet(viewsets.ModelViewSet):
    """Extensiones que pertenecen a la Universidad Alfa y Omega."""

    queryset = Extension.objects.all()
    serializer_class = ExtensionSerializer

    def get_permissions(self):
        """Sobrescribe el método para establecer permisos según la acción."""
        if self.action in ["create", "update", "destroy"]:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [SoloListar]
        return super().get_permissions()

    def perform_create(self, serializer: ExtensionSerializer):
        """Sobrescribe el método para crear una extensión con su dirección."""
        serializer.save()

    def perform_update(self, serializer: ExtensionSerializer):
        """Sobrescribe el método para actualizar una extensión con su dirección."""
        serializer.save()

    def perform_destroy(self, instance: Extension):
        """Sobrescribe el método para eliminar una extensión y su dirección."""
        instance.direccion.delete()
        instance.delete()
