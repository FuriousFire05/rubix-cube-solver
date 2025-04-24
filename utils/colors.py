# utils/colors.py

from enum import Enum

class Color(Enum):
    WHITE  = "#FFFFFF" # White
    YELLOW = "#FFFF00" # Yellow
    BLUE   = "#0000FF" # Blue
    GREEN  = "#00FF00" # Green
    RED    = "#FF0000" # Red
    ORANGE = "#FFA500" # Orange

    def __str__(self):
        return self.name.capitalize()

    def __repr__(self):
        return f"Color.{self.name}"