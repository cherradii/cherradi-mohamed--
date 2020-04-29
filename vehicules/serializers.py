from rest_framework_mongoengine import serializers

from .models import Vehicule



class VehiculeSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Vehicule
        fields = '__all__'