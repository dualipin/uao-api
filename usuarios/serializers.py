from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Usuario


class TokenWithRoleSerializer(TokenObtainPairSerializer):
    """Serializer para el token de acceso con rol del usuario."""

    @classmethod
    def get_token(cls, user: Usuario):
        """Genera el token de acceso con el rol del usuario."""
        token = super().get_token(user)
        # Añade el rol del usuario al token
        token["rol"] = user.rol
        return token
