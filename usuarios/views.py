from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import TokenWithRoleSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom view to obtain JWT token with user role.
    """

    serializer_class = TokenWithRoleSerializer
