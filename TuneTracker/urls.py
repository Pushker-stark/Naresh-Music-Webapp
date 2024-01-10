from django.urls import path
from .views import home,artist,albums,song_upload

urlpatterns = [
    path('', home, name='home'),
    # path('songs/<int:song_id>/', song_detail, name='song_detail'),
    path('artist/', artist, name='artist'),
    path('upload/',song_upload,name='upload'),
    path('album/',albums,name='albums'),
]