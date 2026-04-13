# visualizer/ui_state.py

from core.input_state import InputState

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
        self.mode = "move"

        # Scroll positions
        self.history_offset = 0
        self.solution_offset = 0

        # Animation flag (for future)
        self.is_animating = False

        self.input_state = InputState()