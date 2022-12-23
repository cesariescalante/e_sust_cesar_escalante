from rest_framework import serializers
from platos.models import Platos

class PlatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platos
        fields = ('nombre', 'precio','pais')