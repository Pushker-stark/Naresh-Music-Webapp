from django.shortcuts import render
from .models import Song,Artist

def home(request):
    songs = Song.objects.all()
    return render(request, 'index.html', {'songs': songs})

def artist(request):
    # song = Song.objects.get(pk=song_id)
    artist=Artist.objects.all()
    return render(request, 'artist.html', {'artist': artist})

def song_upload(request):
    return render(request,'form.html')

def albums(request):
    return render(request,'album.html')
