from django.shortcuts import redirect
from django.http import JsonResponse
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
    userProfile = spot.current_user()

    request.session['spotify_auth'] = tokenInfo['access_token']    
    return JsonResponse(userProfile)
