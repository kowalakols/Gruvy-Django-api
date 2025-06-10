from .models import playlist
from music.serializers import MusicSerializer
from rest_framework import serializers

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = playlist
        fields='__all__'
        depth = 1