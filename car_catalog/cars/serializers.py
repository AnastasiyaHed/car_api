from rest_framework import serializers
from .models import Car

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'year', 'price', 'image')

    # Используем serializers.ImageField
    image = serializers.ImageField(max_length=None, use_url=True, required=False)
