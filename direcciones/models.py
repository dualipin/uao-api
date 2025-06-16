from django.db import models


class Direccion(models.Model):
    """Modelo que representa una dirección."""
    municipio = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, default="Tabasco")
    calle = models.CharField(max_length=100)
    numero_exterior = models.CharField(max_length=10, blank=True, null=True)
    colonia = models.CharField(max_length=100, blank=True, null=True)
    codigo_postal = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.calle} {self.numero_exterior}, {self.colonia}, {self.municipio}, {self.estado}, {self.codigo_postal}"
