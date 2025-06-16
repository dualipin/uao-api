from django.db import models
from carreras.models import Carrera
from direcciones.models import Direccion
from extensiones.models import Extension


class Alumno(models.Model):
    matricula = models.CharField(max_length=10)
    curp = models.CharField(max_length=18, unique=True)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(
        max_length=10,
        choices=[("M", "Masculino"), ("F", "Femenino"), ("O", "Otro")],
        default="O",
    )

    direccion = models.OneToOneField(
        Direccion, on_delete=models.CASCADE, related_name="alumnos"
    )

    # contacto
    telefono = models.CharField(max_length=15, unique=True)
    correo_electronico = models.EmailField(unique=True)

    # estado del alumno
    extension = models.OneToOneField(
        Extension, on_delete=models.CASCADE, related_name="alumnos"
    )

    periodo_ingreso = models.SmallIntegerField(
        default=1
    )  # 1: Enero-Junio, 2: Julio-Diciembre

    observaciones = models.TextField(blank=True, null=True)
    semestre = models.IntegerField(default=1)
    carrera = models.ForeignKey(
        Carrera, on_delete=models.CASCADE, related_name="alumnos"
    )
    activo = models.BooleanField(default=True)
    fecha_ingreso = models.DateField(auto_now_add=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["apellido_paterno", "nombre"]


class Bachiller(models.Model):
    alumno = models.OneToOneField(
        Alumno, on_delete=models.CASCADE, related_name="bachiller"
    )
    nombre = models.CharField(max_length=100)
    fecha_egreso = models.DateField()
    promedio = models.DecimalField(max_digits=4, decimal_places=2)
    municipio = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    tipo_bachillerato = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.alumno.nombre} - {self.nombre}"


class Documentacion(models.Model):
    alumno = models.OneToOneField(
        Alumno, on_delete=models.CASCADE, related_name="documentos"
    )
    acta_nacimiento = models.BooleanField(default=False)
    curp = models.BooleanField(default=False)
    certificado_bachillerato = models.BooleanField(default=False)
    certificado_medico = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.alumno.nombre}"

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
        ordering = ["alumno"]
