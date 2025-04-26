# utils/colors.py

from enum import Enum


class Color(Enum):
    # fmt: off
    WHITE   = "#FFFFFF"  # White
    YELLOW  = "#FFFF00"  # Yellow
    BLUE    = "#0000FF"  # Blue
    GREEN   = "#00FF00"  # Green
    RED     = "#FF0000"  # Red
    ORANGE  = "#FFA500"  # Orange
    # fmt: on

    def __str__(self):
        """Return the color name in a readable format."""
        return self.name.capitalize()

    def __repr__(self):
        """Return the color name in a format suitable for debugging."""
        return f"Color.{self.name}"
