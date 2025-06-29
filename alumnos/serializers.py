from rest_framework import serializers
from direcciones.serializers import DireccionSerializer
from .models import Alumno


class AlumnoSerializer(serializers.ModelSerializer):
    direccion = DireccionSerializer()

    class Meta:
        model = Alumno
        fields = "__all__"  # Serializa todos los campos del modelo Alumno
        read_only_fields = ["id"]  # El campo 'id' es de solo lectura
