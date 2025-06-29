from django.contrib import admin
from .models import Estado, Municipio, Direccion


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    """Admin para el modelo Estado."""

    list_display = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("nombre",)


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    """Admin para el modelo Municipio."""

    list_display = ("nombre", "estado")
    search_fields = ("nombre",)
    ordering = ("estado__nombre", "nombre")
    list_filter = ("estado",)


@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    """Admin para el modelo Direccion."""

    list_display = (
        "calle",
        "numero_exterior",
        "numero_interior",
        "colonia",
        "codigo_postal",
        "municipio",
        "estado",
    )
    search_fields = ("calle", "colonia", "codigo_postal")
    ordering = ("municipio__estado__nombre", "municipio__nombre", "calle")
    list_filter = ("municipio__estado", "municipio")
