from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UsuarioManager(BaseUserManager):
    """Manager personalizado para el modelo Usuario."""

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("rol", "admin")
        return self.create_user(username, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    """Modelo que representa a un usuario del sistema."""

    ROLES_CHOICES = (
        ("admin", "Administrador"),
        ("coordinador", "Coordinador"),
        ("profesor", "Profesor"),
        ("administrativo", "Administrativo"),
        ("auxiliar_administrativo", "Auxiliar Administrativo"),
        ("alumno", "Alumno"),
        ("cajero", "Cajero"),
        ("escolar", "Escolar"),
    )

    username = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(
        default=True, help_text="Indica si el usuario está activo."
    )
    is_staff = models.BooleanField(default=False)
    rol = models.CharField(
        max_length=30,
        choices=ROLES_CHOICES,
        default="alumno",
    )
    desde = models.DateTimeField(
        auto_now_add=True, help_text="Fecha de creación del usuario."
    )

    USERNAME_FIELD = "username"

    objects = UsuarioManager()

    def __str__(self):
        return f"{self.username} - {self.rol}"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
