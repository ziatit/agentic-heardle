from tools import get_user_recent_tracks
from state import State

def fetch_tracks_node(state: State) -> dict:
    """Fetches the user's recent tracks from Last.fm and updates the state."""
    recent_tracks = get_user_recent_tracks(limit=5)
    return {"candidate_tracks": recent_tracks}