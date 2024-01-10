from django.shortcuts import render
from .models import Song

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'index.html', {'songs': songs})

# def song_detail(request, song_id):
#     song = Song.objects.get(pk=song_id)
#     return render(request, 'music/song_detail.html', {'song': song})
