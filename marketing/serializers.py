from rest_framework_mongoengine import serializers

from .models import Mark



class MarkSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Mark
        fields = '__all__'