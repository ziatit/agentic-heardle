import pylast
from dotenv import load_dotenv
from os import getenv

def get_lastfm_client():
    """Returns a Last.fm client using the credentials from the .env file."""
    load_dotenv()
    api_key = getenv('PYLAST_API_KEY')
    api_secret = getenv('PYLAST_API_SECRET')
    username = getenv('PYLAST_USERNAME')
    
    return pylast.LastFMNetwork(api_key=api_key, api_secret=api_secret, username=username)

def get_user_recent_tracks(limit=5):
    client = get_lastfm_client()
    user_tracks = client.get_user(client.username).get_recent_tracks(limit=limit)
    tracks = [
        {
            'name': song.track.get_name(),
            'artist': song.track.get_artist().get_name(),
            'album': song.album if song.album else None,
        } for song in user_tracks
    ]

    return tracks