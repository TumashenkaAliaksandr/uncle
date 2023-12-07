from django.shortcuts import render

# Create your views here.
def index(request):
    """Main page music site ДяДя"""
    return render(request, 'webapp/index.html')


def albums(request):
    """Album page music site ДяДя"""
    return render(request, 'webapp/album.html')