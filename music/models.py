from django.db import models

class music(models.Model):
    cover_img = models.URLField()
    song_name = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=10)
    lyrics = models.TextField()
    release_date = models.DateField(auto_now_add=True)
    producer = models.CharField(max_length=30)
    song_url = models.URLField()

def __str__(self):
        return self
