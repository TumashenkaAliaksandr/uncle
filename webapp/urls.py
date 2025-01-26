from django.urls import path

from webapp import views
from webapp.views import *
from django.conf import settings
from django.conf.urls.static import static


app_name = 'webapp'


urlpatterns = [
    path('', index, name='home'),
    path('albums', albums, name='albums'),
    path('api/songs/', views.get_songs, name='get_songs'),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
