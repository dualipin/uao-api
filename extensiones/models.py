from django.db import models
from direcciones.models import Direccion


class Extension(models.Model):
    """Modelo que representa una extensión de Alfa y Omega."""

    nombre = models.CharField(max_length=100, unique=True)
    contacto = models.CharField("Numero de Contacto", max_length=20)
    direccion = models.ForeignKey(
        Direccion, on_delete=models.CASCADE, related_name="extensiones"
    )

    def __str__(self):
        return f"Extension {self.nombre} - ({self.direccion})"
