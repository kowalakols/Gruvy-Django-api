from rest_framework.serializers import ModelSerializer
from ..models import User
from music.serializers import MusicSerializer
from playlist.serializers import PlaylistSerializer

class ProfileSerializer(ModelSerializer):
    musics = MusicSerializer(many=True)
    playlist = PlaylistSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'location', 'is_staff']