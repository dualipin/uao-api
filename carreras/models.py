from django.db import models
from extensiones.models import Extension


class Carrera(models.Model):
    """Modelo que representa una carrera universitaria."""

    TIPOS_CARRERA = [
        ("Licenciatura", "Licenciatura"),
        ("Maestría", "Maestría"),
        ("Doctorado", "Doctorado"),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(
        max_length=30,
        blank=True,
        choices=TIPOS_CARRERA,
        default="Licenciatura",
    )
    abreviatura = models.CharField(
        max_length=10,
        default="",
        blank=True,
        help_text="Abreviatura de la carrera, por ejemplo: 'II'.",
        unique=True,
    )
    plan = models.CharField(
        max_length=50,
        help_text="Plan de estudios de la carrera, por ejemplo: 'Plan 2023'.",
        default="plan-actual",
    )
    extensiones = models.ManyToManyField(
        Extension,
        related_name="carreras",
        blank=True,
        help_text="Extensiones donde esta disponible esta carrera.",
    )
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.plan} - {self.nombre}"
