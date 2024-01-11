from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Song,Artist
from .forms import SongForm

def home(request):
    songs = Song.objects.all()[:8]
    return render(request, 'index.html', {'songs': songs})

def artist(request):
    # song = Song.objects.get(pk=song_id)
    artist=Artist.objects.all()
    return render(request, 'artist.html', {'artist': artist})

def artist_song(request,artist_name):

    try:
        artistname = Artist.objects.get(name__iexact=artist_name)
        songs = Song.objects.filter(artist=artistname)
    except Artist.DoesNotExist:
        songs = []

    song_cnt=songs.count()

    params = {'songs': songs, 'artistname':artistname,'song_cnt':song_cnt}
    return render(request,'artist_song.html',params)

def albums(request):
    songs = Song.objects.all()
    return render(request,'album.html',{'songs':songs})

def song_upload(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        artist=request.POST.get('artist')
        songurl=request.POST.get('songurl')
        imageurl=request.POST.get('imageurl')

        artistname=''
        try:
            artistname = Artist.objects.get(name__iexact=artist)
            # Perform actions when artist is found
        except Artist.DoesNotExist:
            art=Artist(name=artist)
            art.save()
            artistname=artist
            # Handle the case when the artist is not found
            # You might want to return an HTTP 404 response or render an error page
        song = Song(title=title,artist=artistname,songurl=songurl,imageurl=imageurl)
        song.save()
        # if form.is_valid():
        #     form.save()

        print("save the data")
        return redirect('home')  # Redirect to a success page or another URL
        # else:
        #     print(form.errors)
    else:
        form = SongForm()
        messages.warning(request, "No submitted!!")

    return render(request, 'form.html', {'form': form})

