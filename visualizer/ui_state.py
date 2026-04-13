# visualizer/ui_state.py

"""
ui_state.py

UI state container for the Rubik's Cube application.

This module defines the UIState class, which stores transient interface state
separately from the live cube engine.

It tracks:
- current mode (move or input)
- selected input color
- solution and scroll state
- status messages
- temporary draft cube used during input mode
"""

class UIState:
    def __init__(self):
        # Mode: "move" or "input"
        self.mode = "move"

        # Selected color for input mode
        self.selected_color = None

        # Solution and scramble tracking
        self.solution_moves = []
        self.scramble_moves = []

        # UI status message
        self.status_message = "Ready"

        # Scroll positions
        self.history_offset = 0
        self.solution_offset = 0

        # Temporary editable cube used during input mode
        self.draft_cube = None