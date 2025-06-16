from rest_framework import serializers
from .models import Direccion

class DireccionSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Direccion."""
    
    class Meta:
        model = Direccion
        fields = '__all__'