from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='album_covers', blank=True, null=True)

    def __str__(self):
        return self.title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='song_files', blank=False)
    video_file = models.FileField(upload_to='video_files', blank=True, null=True)

    def __str__(self):
        return self.title

