# utils/faces.py

from enum import Enum
from utils.colors import Color

class Face(Enum):
    U = Color.YELLOW  # Up face is Yellow
    D = Color.WHITE   # Down face is White
    F = Color.BLUE    # Front face is Blue
    B = Color.GREEN   # Back face is Green
    L = Color.ORANGE  # Left face is Orange
    R = Color.RED     # Right face is Red

    def __str__(self):
        return self.name.capitalize()

    def __repr__(self):
        return f"Face.{self.name}"