from rest_framework.serializers import ModelSerializer
from ..models import User
from music.serializers.common import SkillSerializer
from playlist.serializers.common import CharitySerializer

class ProfileSerializer(ModelSerializer):
    musics = musicSerializer(many=True)
    playlist = playlistSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'location', 'is_staff', 'music', 'charities']