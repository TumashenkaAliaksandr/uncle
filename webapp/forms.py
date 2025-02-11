from django import forms
from .models import Album, Song, Release, SongRelease


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('title', 'artist', 'release_date', 'cover_image')

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('title', 'audio_file', 'video_file')


class ReleaseForm(forms.ModelForm):
    class Meta:
        model = Release
        fields = ('title', 'artist', 'release_date', 'cover_image')

class SongReleaseForm(forms.ModelForm):
    class Meta:
        model = SongRelease
        fields = ('title', 'audio_file', 'video_file')
