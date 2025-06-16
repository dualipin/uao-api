from rest_framework import serializers
from direcciones.serializers import DireccionSerializer
from .models import Alumno, Bachiller, Documentacion


class BachillerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bachiller
        exclude = ["alumno"]


class DocumentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentacion
        exclude = ["alumno"]


class AlumnoSerializer(serializers.ModelSerializer):
    bachiller = BachillerSerializer()
    documentos = DocumentacionSerializer()
    direccion = DireccionSerializer()

    class Meta:
        model = Alumno
        fields = "__all__"
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['extension'] = instance.extension.nombre if instance.extension else None
        return representation

    def create(self, validated_data):
        bachiller_data = validated_data.pop("bachiller", None)
        documentos_data = validated_data.pop("documentos", None)
        direccion_data = validated_data.pop("direccion", None)

        if direccion_data:
            # Crear la dirección asociada al alumno
            direccion_serializer = DireccionSerializer(data=direccion_data)
            direccion_serializer.is_valid(raise_exception=True)
            direccion = direccion_serializer.save()
        else:
            raise serializers.ValidationError(
                {"direccion": "La dirección es obligatoria."}
            )

        alumno = Alumno.objects.create(direccion=direccion, **validated_data)

        # Crear automáticamente documentacion y bachiller
        if documentos_data:
            Documentacion.objects.create(alumno=alumno, **documentos_data)
        else:
            Documentacion.objects.create(alumno=alumno)

        if bachiller_data:
            Bachiller.objects.create(alumno=alumno, **bachiller_data)
        else:
            Bachiller.objects.create(
                alumno=alumno,
                nombre="",
                fecha_egreso="2000-01-01",
                promedio=0.0,
                municipio="",
                estado="",
                tipo_bachillerato="",
            )

        return alumno

    def update(self, instance, validated_data):
        bachiller_data = validated_data.pop("bachiller", None)
        documentos_data = validated_data.pop("documentos", None)
        direccion_data = validated_data.pop("direccion", None)

        # Actualizar la dirección
        if direccion_data:
            direccion_serializer = DireccionSerializer(
                instance.direccion, data=direccion_data, partial=True
            )
            direccion_serializer.is_valid(raise_exception=True)
            direccion_serializer.save()

        # Actualizar el alumno
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Actualizar documentos
        if documentos_data:
            Documentacion.objects.update_or_create(
                alumno=instance, defaults=documentos_data
            )

        # Actualizar bachiller
        if bachiller_data:
            Bachiller.objects.update_or_create(
                alumno=instance, defaults=bachiller_data
            )

        return instance
    
    