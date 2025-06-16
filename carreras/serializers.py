from rest_framework import serializers
from extensiones.serializers import ExtensionSerializer
from .models import Carrera, CarreraExtension


class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = "__all__"


class CarreraExtensionSerializer(serializers.ModelSerializer):
    carrera = CarreraSerializer(read_only=True)
    extension = ExtensionSerializer(read_only=True)

    class Meta:
        model = CarreraExtension
        fields = ["id", "carrera", "extension"]
