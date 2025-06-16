from rest_framework import permissions


class SoloListar(permissions.BasePermission):
    """Cualquier usuario puede listar los objetos de este modelo."""

    def has_permission(self, request, view):
        return request.method == "GET"


class SuperAdmin(permissions.BasePermission):
    """Permite el acceso solo a superusuarios."""

    def has_permission(self, request, view):
        """Verifica si el usuario es un superusuario."""
        return request.user and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        """Verifica si el usuario es un superusuario para el objeto."""
        return request.user and request.user.is_superuser
