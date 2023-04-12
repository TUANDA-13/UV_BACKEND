from .models import UV
from rest_framework import serializers


class UVSerializer(serializers.ModelSerializer):
    class Meta:
        model = UV
        fields = '__all__'
        
    def create(self, validated_data):
        uv = UV.objects.create(
            id_esp=validated_data['id_esp'],
            x=validated_data['x'],
            y=validated_data['y'],
        )
        return uv
    
