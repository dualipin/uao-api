from django.db import models
from alumnos.models import Alumno
from uuid import uuid4


class Conceptos(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Pagos(models.Model):
    TIPO_PAGO_CHOICES = [
        ("ef", "Efectivo"),
        ("tr", "Transferencia"),
        ("ot", "Otro"),
    ]

    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name="pagos")
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(
        max_length=50, choices=TIPO_PAGO_CHOICES, default="ef"
    )
    semestre = models.IntegerField()
    concepto = models.ForeignKey(
        Conceptos, on_delete=models.CASCADE, related_name="pagos", blank=True, null=True
    )
    folio_pago = models.UUIDField(
        max_length=100, unique=True, editable=False, default=uuid4
    )
    observaciones = models.TextField(blank=True, null=True)

    # Timestamps
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago de {self.alumno.nombre} - {self.fecha_pago} - {self.monto} {self.metodo_pago}"

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
        ordering = ["-fecha_pago"]
