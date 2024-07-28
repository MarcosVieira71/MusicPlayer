from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse
from .helper import getSpotifyOAuth
from spotipy import Spotify

def spotifyAuth(request):
    spAuth = getSpotifyOAuth()
    auth_url = spAuth.get_authorize_url()  
    return redirect(auth_url)

def spotifyCallback(request):
    code = request.GET.get('code')
    if not code:
        return JsonResponse({'error': 'No authorization code provided'}, status=400)

    spAuth = getSpotifyOAuth()
    tokenInfo = spAuth.get_access_token(code, check_cache=False) 

    if not tokenInfo:
        return JsonResponse({'error': 'Failed to retrieve access token'}, status=400)

    spot = Spotify(auth=tokenInfo['access_token'])
    request.session['spotify_auth'] = tokenInfo['access_token']    
    return redirect('playlists')

def home(request):
    return render(request, 'home.html')

def playlists(request):
    access_token = request.session.get('spotify_auth')
    if not access_token:
        return redirect('home') 
    sp = Spotify(auth=access_token)

    playlists = sp.current_user_playlists()
    playlist_items = playlists['items'] 
    return render(request, 'playlists.html', {'playlists': playlist_items})

def playlist_details(request, playlist_id):
    access_token = request.session.get('spotify_auth')
    if not access_token:
        return redirect('home')

    sp = Spotify(auth=access_token)

    playlist = sp.playlist(playlist_id)
    tracks = playlist['tracks']['items']  
    return render(request, 'playlist_data.html', {'playlist': tracks})
