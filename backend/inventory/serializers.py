from rest_framework import serializers
from .models import TextileWaste


class TextileWasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextileWaste
        fields = '__all__'
