from spotipy.oauth2 import SpotifyOAuth
from django.conf import settings


def getSpotifyOAuth():
    return SpotifyOAuth(
        client_id=settings.SPOTIPY_CLIENT_ID,
        client_secret=settings.SPOTIPY_CLIENT_SECRET,
        redirect_uri=settings.SPOTIPY_REDIRECT_URI,
        scope=settings.SPOTIPY_SCOPE,
        cache_path=None)