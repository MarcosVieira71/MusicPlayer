from django.urls import path
from . import views 

urlpatterns = [
    path('auth/', views.spotifyAuth,name='spotify-auth'),
    path('callback/',views.spotifyCallback,name='spotify-callback'),
    path('logout/',views.logout,name='spotify-logout')
]