from rest_framework_mongoengine import serializers

from .models import Trav



class TravSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Trav
        fields = '__all__'