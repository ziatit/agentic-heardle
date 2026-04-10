from langgraph.graph import StateGraph, END
from state import State
from nodes import fetch_tracks_node

workflow = StateGraph(State)

workflow.add_node("fetch tracks",fetch_tracks_node)

workflow.set_entry_point( "fetch tracks")
workflow.add_edge("fetch tracks", END)

app = workflow.compile()