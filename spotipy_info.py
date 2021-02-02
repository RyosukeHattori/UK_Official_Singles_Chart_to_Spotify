import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

def spotipy_info():
    with open("bin/my_ID.txt") as f:
        l = f.readlines()

    token = util.prompt_for_user_token(
    username=l[0],
    scope='user-read-playback-state,playlist-read-private,user-modify-playback-state,playlist-modify-public', 
    client_id = l[1],
    client_secret = l[2],
    redirect_uri="http://localhost:8889/callback")
    
    return spotipy.Spotify(auth=token)
   