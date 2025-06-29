from django.db import models
from uuid import uuid4

from direcciones.models import Direccion
from carreras.models import CarreraExtension


class Alumno(models.Model):
    """Modelo que representa a un alumno."""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    # Datos personales
    matricula = models.CharField(max_length=15)
    curp = models.CharField(max_length=18, unique=True)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(
        max_length=1,
        choices=[
            ("M", "Masculino"),
            ("F", "Femenino"),
            ("O", "Otro"),
        ],
        default="O",
    )

    # Contacto
    telefono = models.CharField(max_length=12, blank=True, null=True)
    correo = models.EmailField(unique=True)

    direccion = models.ForeignKey(
        Direccion,
        on_delete=models.CASCADE,
        related_name="alumnos",
        null=True,
        blank=True,
    )

    # Información académica
    carrera = models.ForeignKey()

    # Fecha de creación y actualización
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        apellido_materno = self.apellido_materno if self.apellido_materno else ""

        return f"{self.nombre} {self.apellido_paterno} {apellido_materno}".strip()
