from .serializers import CarreraSerializer
from .models import Carrera
from rest_framework import viewsets


class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer
