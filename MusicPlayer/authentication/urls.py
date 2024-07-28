from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('auth/', views.spotifyAuth,name='spotify-auth'),
    path('callback/',views.spotifyCallback,name='spotify-callback'),
    path('playlists', views.playlists, name='playlists'),
    path('playlist/<str:playlist_id>', views.playlist_details, name='playlist_details'),
]