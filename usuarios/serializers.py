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


class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False, allow_blank=True, write_only=True)

    class Meta:
        model = Usuario
        # fields = "__all__"
        exclude = (
            "groups",
            "user_permissions",
            "last_login",
            "is_superuser",
            "is_staff",
        )

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        usuario = super().create(validated_data)
        if password:
            usuario.set_password(password)
            usuario.save()
        return usuario

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        usuario = super().update(instance, validated_data)
        if password:
            usuario.set_password(password)
            usuario.save()
        return usuario
