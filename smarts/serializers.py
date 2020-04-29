from rest_framework_mongoengine import serializers

from .models import Smart



class SmartSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Smart
        fields = '__all__'