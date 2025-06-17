from .models import playlist, music
from music.serializers import MusicSerializer
from rest_framework import serializers

class PlaylistSerializer(serializers.ModelSerializer):
    songs = MusicSerializer(
         many=True,
         required=False
    )
    song_id = serializers.IntegerField(write_only=True, required=False)
    remove_song_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = playlist
        fields='__all__'
        read_only_fields = ['owner']
        depth = 1

    def create(self, validated_data):
        songs = validated_data.pop('songs', [])
        playlist_instance = playlist.objects.create(**validated_data)
        playlist_instance.songs.set(songs)
        return playlist_instance


    def update(self, instance, validated_data):
        song_id = validated_data.pop('song_id', None)
        if song_id:
            try:
                song = music.objects.get(id=song_id)
                instance.songs.add(song)
            except music.DoesNotExist:
                raise serializers.ValidationError({"song_id": "Invalid song ID"})
            
        remove_song_id = validated_data.pop('remove_song_id', None)
        if remove_song_id:
            try:
                song = music.objects.get(id=remove_song_id)
                instance.songs.remove(song)
            except music.DoesNotExist:
                raise serializers.ValidationError({"remove_song_id": "Invalid song ID"})
        
        instance.save()
        return instance