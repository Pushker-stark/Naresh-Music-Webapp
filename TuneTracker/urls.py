from django.urls import path
from .import views
from .views import home,artist,albums,song_upload

urlpatterns = [
    path('', home, name='home'),
    # path('songs/<int:song_id>/', song_detail, name='song_detail'),
    path('artist/', views.artist, name='artist'),
    path('artist_songs/<str:artist_name>/', views.artist_song, name='artist_song'),
    path('upload/',song_upload,name='upload'),
    path('album/',albums,name='albums'),
]