from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='album_covers', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "АЛЬБОМЫ"
        verbose_name_plural = "АЛЬБОМЫ"

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='song_files', blank=False)
    video_file = models.FileField(upload_to='video_files', blank=True, null=True)
    photo_file = models.ImageField(upload_to='photo_files_songs', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "ПЕСНИ"
        verbose_name_plural = "ПЕСНИ"


class Release(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='album_covers', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "РЕЛИЗЫ"
        verbose_name_plural = "РЕЛИЗЫ"

class SongRelease(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name='songs_releases')
    title = models.CharField(max_length=200)
    audio_file_release = models.FileField(upload_to='song_files_release', blank=False)
    video_file_release = models.FileField(upload_to='video_files_release', blank=True, null=True)
    photo_file_release = models.ImageField(upload_to='photo_files_songs_release', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "РЕЛИЗ ПЕСНИ"
        verbose_name_plural = "РЕЛИЗ ПЕСНИ"
