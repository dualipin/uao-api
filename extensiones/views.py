from rest_framework import viewsets
from .serializers import ExtensionSerializer
from .models import Extension


class ExtensionViewSet(viewsets.ModelViewSet):
    """Extensiones que pertenecen a la Universidad Alfa y Omega."""

    queryset = Extension.objects.all()
    serializer_class = ExtensionSerializer

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
