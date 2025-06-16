from django.db import models
from extensiones.models import Extension


class Carrera(models.Model):
    TIPOS_CARRERA = [
        ("Licenciatura", "Licenciatura"),
        ("Maestría", "Maestría"),
        ("Doctorado", "Doctorado"),
    ]

    nombre = models.CharField(max_length=100, unique=True)
    abreviatura = models.CharField(max_length=10, unique=True)
    tipo = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=TIPOS_CARRERA,
        default="Licenciatura",
    )
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class CarreraExtension(models.Model):
    carrera = models.ForeignKey(
        Carrera, on_delete=models.CASCADE, related_name="carreras_extension"
    )
    extension = models.ForeignKey(
        Extension, on_delete=models.CASCADE, related_name="carreras_extension"
    )

    class Meta:
        verbose_name = "Carrera por Extensión"
        verbose_name_plural = "Carreras por Extensión"
        unique_together = ("carrera", "extension")

    def __str__(self):
        return f"{self.carrera.nombre} - {self.extension.nombre}"