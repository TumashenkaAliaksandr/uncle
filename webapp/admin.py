from django.contrib import admin
from .models import Album, Song

class SongInline(admin.TabularInline):
    model = Song
    extra = 0

class AlbumAdmin(admin.ModelAdmin):
    inlines = [SongInline]
    list_display = ('title', 'artist', 'release_date')

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'album')

admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
