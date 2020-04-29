from rest_framework_mongoengine import serializers

from .models import Covid



class CovidSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Covid
        fields = '__all__'