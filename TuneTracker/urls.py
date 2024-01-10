from django.urls import path
from .views import song_list

urlpatterns = [
    path('', song_list, name='songlist'),
    # path('songs/<int:song_id>/', song_detail, name='song_detail'),
]