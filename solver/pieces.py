# solver/pieces.py

from utils.colors import Color
from utils.faces import Face
from typing import Dict, Tuple


class Piece:
    def __init__(
        self, colors: Dict[Color, Face], name: str, position: Tuple[int, int, int]
    ):
        """
        :param colors: A dictionary mapping colors to faces (e.g., {Color.YELLOW: Face.U})
        :param position: 3D tuple (x, y, z) representing the position in the 3x3x3 Rubik's cube grid
        """
        self.colors = colors  # The color on each face of the piece
        self.position = position  # Position in 3D space (x, y, z)
        self.name = name

    def __repr__(self):
        """String representation of the piece for debugging."""
        return f"{self.__class__.__name__}(Colors: {self.colors}, Position: {self.position})"

    def get_position(self) -> Tuple[int, int, int]:
        """Return the position of the piece."""
        return self.position

    def set_position(self, position: Tuple[int, int, int]):
        """Update the position of the piece."""
        self.position = position

    def get_faces(self):
        """Return the color-face map (colors assigned to each face)."""
        return self.colors

    def set_faces(self, c: Dict[Color, Face]):
        """Update the color-face map."""
        temp = self.colors.copy()
        for color, face in zip(temp.keys(), c.values()):
            self.colors[color] = face

    def get_name(self) -> str:
        """Return the name of the piece."""
        return self.name
    
    def set_name(self, name: str):
        """Update the name of the piece."""
        self.name = name


class Center(Piece):
    def __init__(
        self, colors: Dict[Color, Face], name: str, position: Tuple[int, int, int]
    ):
        # Center piece must have exactly 1 face and color
        if len(colors) != 1:
            raise ValueError("Center piece must have exactly 1 color and 1 face.")
        super().__init__(colors, name, position)


class Edge(Piece):
    def __init__(
        self, colors: Dict[Color, Face], name: str, position: Tuple[int, int, int]
    ):
        # Edge piece must have exactly 2 faces and colors
        if len(colors) != 2:
            raise ValueError("Edge piece must have exactly 2 colors and 2 faces.")
        super().__init__(colors, name, position)


class Corner(Piece):
    def __init__(
        self, colors: Dict[Color, Face], name: str, position: Tuple[int, int, int]
    ):
        # Corner piece must have exactly 3 faces and colors
        if len(colors) != 3:
            raise ValueError("Corner piece must have exactly 3 colors and 3 faces.")
        super().__init__(colors, name, position)
