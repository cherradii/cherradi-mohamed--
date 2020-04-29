from rest_framework_mongoengine import serializers

from .models import Big



class BigSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Big
        fields = '__all__'