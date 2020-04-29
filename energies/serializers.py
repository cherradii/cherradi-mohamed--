from rest_framework_mongoengine import serializers

from .models import Energy



class EnergySerializer(serializers.DocumentSerializer):
    class Meta:
        model = Energy
        fields = '__all__'