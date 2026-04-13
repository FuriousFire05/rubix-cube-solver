# core/input_state.py

class InputState:
    """
    Represents a manually editable cube state (sticker-based),
    independent from the RubiksCube engine.
    """

    def __init__(self):
        self.reset()

    def reset(self):
        # Default solved colors
        self.faces = {
            "U": [["W"] * 3 for _ in range(3)],
            "D": [["Y"] * 3 for _ in range(3)],
            "F": [["G"] * 3 for _ in range(3)],
            "B": [["B"] * 3 for _ in range(3)],
            "L": [["O"] * 3 for _ in range(3)],
            "R": [["R"] * 3 for _ in range(3)],
        }

    def set_color(self, face: str, row: int, col: int, color: str):
        """
        Set color of a sticker, excluding center pieces.
        """
        if (row, col) == (1, 1):
            return  # lock center

        self.faces[face][row][col] = color

    def get_color(self, face: str, row: int, col: int) -> str:
        return self.faces[face][row][col]

    def get_all_faces(self):
        return self.faces