from django.db import models
from django.core.validators import RegexValidator


class Estado(models.Model):
    """Modelo que representa un estado de la República Mexicana."""

    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.strip().lower()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ["nombre"]


class Municipio(models.Model):
    """Modelo que representa un municipio de un estado de la República Mexicana."""

    nombre = models.CharField(max_length=100)
    estado = models.ForeignKey(
        Estado, on_delete=models.CASCADE, related_name="municipios"
    )

    def __str__(self):
        return f"{self.nombre}, {self.estado.nombre}"

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
        ordering = ["estado", "nombre"]


class Direccion(models.Model):
    """Modelo que representa una dirección."""

    municipio = models.ForeignKey(
        Municipio, on_delete=models.PROTECT, related_name="direcciones"
    )
    calle = models.CharField(max_length=100)
    numero_exterior = models.CharField(max_length=10, blank=True, null=True)
    numero_interior = models.CharField(max_length=10, blank=True, null=True)
    colonia = models.CharField(max_length=100, blank=True, null=True)
    codigo_postal = models.CharField(
        max_length=5,
        validators=[
            RegexValidator(
                regex=r"^\d{5}$",
                message="El código postal debe tener 5 dígitos.",
                code="invalid_codigo_postal",
            )
        ],
    )

    @property
    def estado(self):
        """Devuelve el estado asociado a la dirección."""
        return self.municipio.estado

    def __str__(self):
        ni = self.numero_interior if self.numero_interior else ""
        ne = self.numero_exterior if self.numero_exterior else "SN"
        colonia = self.colonia if self.colonia else "N/A"

        return f"{self.calle} {ne} {ni}, {colonia}, {self.codigo_postal}, {self.municipio.nombre}, {self.estado}"

    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"
        ordering = ["municipio", "calle"]
