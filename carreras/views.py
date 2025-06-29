from rest_framework import viewsets
from .serializers import CarreraSerializer
from .models import Carrera


class CarreraViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Carreras.
    """

    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned carreras to a given user,
        by filtering against a `user` query parameter in the URL.
        """
        queryset = super().get_queryset()
        user = self.request.query_params.get("user", None)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset
