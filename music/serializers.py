from rest_framework.permissions import AllowAny
from rest_framework import serializers
from .models import music

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = music
        fields = '__all__'
        permission_classes = [AllowAny]