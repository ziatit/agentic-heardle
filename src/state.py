from typing import List, TypedDict, Annotated, Optional, Any
import operator

class State(TypedDict):
    """State is a dictionary that holds the state of the application."""
    
    user_desc: str
    lastfm_id: str
    
    candidate_tracks: Annotated[List[dict], operator.add]
    selected_tracks: Optional[dict]

    attempts: int
    is_solved: bool
