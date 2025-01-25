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