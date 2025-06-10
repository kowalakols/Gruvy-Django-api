from django.db import models
from music.models import music

# Create your models here.
class playlist (models.Model):
    playlist_name = models.CharField(max_length=100)
    songs = models.ManyToManyField(
        to= music,
        related_name='playlists',
    )
    

    def __str__(self):
        return f"{self.playlist_name} ({self.songs.count()} songs)"

