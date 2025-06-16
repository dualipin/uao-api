from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UsuarioManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(activo=True)

    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("tipo", "superadmin")
        return self.create_user(username, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    TIPO_CHOICES = (
        ("alumno", "Alumno"),
        ("profesor", "Profesor"),
        ("administrador", "Administrador"),
        ("superadmin", "Super Administrador"),
        ("usuario", "Usuario"),
    )

    username = models.CharField(max_length=20, unique=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default="alumno")
    activo = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    objects = UsuarioManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username
