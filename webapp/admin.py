from django.contrib import admin
from .models import Album, Song, SongRelease, Release


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


class SongReleaseInline(admin.TabularInline):
    model = SongRelease
    extra = 0

class ReleaseAdmin(admin.ModelAdmin):
    inlines = [SongReleaseInline]
    list_display = ('title', 'artist', 'release_date')

class SongReleaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'release')

admin.site.register(Release, ReleaseAdmin)
admin.site.register(SongRelease, SongReleaseAdmin)