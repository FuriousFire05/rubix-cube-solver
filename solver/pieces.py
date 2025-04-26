# solver/pieces.py

from utils.colors import Color
from utils.faces import Face
from typing import Dict, Tuple


class Piece:
    def __init__(self, colors: Dict[Face, Color], position: Tuple[int, int, int]):
        """
        :param colors: A dictionary mapping faces to colors (e.g., {Face.U: Color.YELLOW})
        :param position: 3D tuple (x, y, z) representing the position in the 3x3x3 Rubik's cube grid
        """
        self.colors = colors  # The color on each face of the piece
        self.position = position  # Position in 3D space (x, y, z)

    def __repr__(self):
        """String representation of the piece for debugging."""
        return f"{self.__class__.__name__}(Colors: {self.colors}, Position: {self.position})"

    def set_position(self, position: Tuple[int, int, int]):
        """Update the position of the piece."""
        self.position = position

    def get_faces(self):
        """Return the face-color map (colors assigned to each face)."""
        return self.colors


class Center(Piece):
    def __init__(self, colors: Dict[Face, Color], position: Tuple[int, int, int]):
        # Center piece must have exactly 1 face and color
        if len(colors) != 1:
            raise ValueError("Center piece must have exactly 1 color and 1 face.")
        super().__init__(colors, position)


class Edge(Piece):
    def __init__(self, colors: Dict[Face, Color], position: Tuple[int, int, int]):
        # Edge piece must have exactly 2 faces and colors
        if len(colors) != 2:
            raise ValueError("Edge piece must have exactly 2 colors and 2 faces.")
        super().__init__(colors, position)


class Corner(Piece):
    def __init__(self, colors: Dict[Face, Color], position: Tuple[int, int, int]):
        # Corner piece must have exactly 3 faces and colors
        if len(colors) != 3:
            raise ValueError("Corner piece must have exactly 3 colors and 3 faces.")
        super().__init__(colors, position)
