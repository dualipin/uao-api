from rest_framework import serializers
from .models import Direccion, Estado, Municipio


class EstadoSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Estado."""

    class Meta:
        model = Estado
        fields = "__all__"


class MunicipioSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Municipio."""

    estado = EstadoSerializer()

    class Meta:
        model = Municipio
        fields = "__all__"


class DireccionSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Direccion."""

    municipio = MunicipioSerializer()

    class Meta:
        model = Direccion
        fields = "__all__"

    def to_representation(self, instance: Direccion):
        data = super().to_representation(instance)
        data["municipio"] = instance.municipio.nombre
        data["estado"] = instance.estado.nombre.title()
        data.pop("id", None)  # Eliminar el campo 'id' si no es necesario

        return data

    def create(self, validated_data):
        """Crear una nueva dirección."""
        municipio_data = validated_data.pop("municipio", None)
        if municipio_data:
            estado_data = municipio_data.pop("estado", None)
            if estado_data:
                # Si se proporciona un estado, crearlo o obtenerlo

                estado_data["nombre"] = estado_data.get("nombre", "").strip()

                estado, _ = Estado.objects.get_or_create(**estado_data)
                municipio, _ = Municipio.objects.get_or_create(
                    estado=estado, **municipio_data
                )
            else:
                municipio, _ = Municipio.objects.get_or_create(**municipio_data)
            validated_data["municipio"] = municipio
        return super().create(validated_data)
