from rest_framework import serializers
from .models import Carrera


class CarreraSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Carrera."""

    class Meta:
        model = Carrera
        fields = "__all__"  # Serializa todos los campos del modelo Carrera
        read_only_fields = ["id"]  # El campo 'id' es de solo lectura

    def to_representation(self, instance: Carrera):
        """Personaliza la representación del objeto Carrera."""
        representation = super().to_representation(instance)

        representation["extensiones"] = [
            ext.nombre for ext in instance.extensiones.all()
        ]
        return representation
