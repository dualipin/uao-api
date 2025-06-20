from rest_framework import serializers
from direcciones.serializers import DireccionSerializer
from direcciones.models import Direccion
from .models import Extension


class ExtensionSerializer(serializers.ModelSerializer):
    """Serializer para crear una extensión."""

    direccion = DireccionSerializer()

    class Meta:
        model = Extension
        fields = "__all__"

    def create(self, validated_data):
        direccion_data = validated_data.pop("direccion")
        direccion = Direccion.objects.create(**direccion_data)
        return Extension.objects.create(direccion=direccion, **validated_data)

    def update(self, instance, validated_data):
        direccion_data = validated_data.pop("direccion", None)
        if direccion_data:
            for attr, value in direccion_data.items():
                setattr(instance.direccion, attr, value)
            instance.direccion.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

    # def to_representation(self, instance):
    #     """Sobrescribe el método para incluir la dirección en la representación."""
    #     representation = super().to_representation(instance)
    #     representation["direccion"] = DireccionSerializer(instance.direccion).data
    #     return representation
