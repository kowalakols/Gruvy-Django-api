from .models import playlist, music
from music.serializers import MusicSerializer
from rest_framework import serializers

class PlaylistSerializer(serializers.ModelSerializer):
    songs = MusicSerializer(
         many=True,
         required=False
    )

    class Meta:
        model = playlist
        fields='__all__'
        read_only_fields = ['owner']
        depth = 1

    # def create(self, validated_data):
    #     songs = validated_data.pop('songs', [])
    #     playlist_instance = playlist.objects.create(**validated_data)
    #     playlist_instance.songs.set(songs)
    #     return playlist_instance