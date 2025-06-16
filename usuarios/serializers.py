from rest_framework import serializers
from .models import Usuario


class PerfilAlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ("username", "tipo", "groups")
        read_only_fields = ("username", "tipo", "groups")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["roles"] = list(instance.groups.values_list("name", flat=True))
        return representation


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ("username", "tipo", "groups")
        read_only_fields = ("username", "tipo", "groups")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["roles"] = list(instance.groups.values_list("name", flat=True))
        return representation
