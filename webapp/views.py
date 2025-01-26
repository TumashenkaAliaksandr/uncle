from django.http import JsonResponse
from django.shortcuts import render

from webapp.models import Album, Song


# Create your views here.
def index(request):
    """Main page music site ДяДя"""
    music_album = Album.objects.all()
    songs = Song.objects.all()
    context = {
        'music_album': music_album,
        'songs': songs,
    }
    return render(request, 'webapp/index.html', context=context)


def albums(request):
    """Album page music site ДяДя"""
    return render(request, 'webapp/album.html')


def get_songs(request):
    songs = Song.objects.all()
    song_list = [
        {
            "image": song.photo_file.url if song.photo_file else "",  # Получаем URL изображения
            "title": song.title,
            "artist": song.album.artist if song.album else "Unknown Artist",  # Получаем имя артиста из альбома
            "mp3": song.audio_file.url if song.audio_file else "",  # Получаем URL MP3 файла
            "oga": song.video_file.url if song.video_file else "",  # Получаем URL OGA файла (если он есть)
        }
        for song in songs
    ]
    return JsonResponse(song_list, safe=False)