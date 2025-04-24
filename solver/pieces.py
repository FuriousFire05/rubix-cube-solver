# solver/pieces.py

class Piece:
    def __init__(self, colors, position=None):
        # colors will be a dictionary with face names as keys and the corresponding colors as values
        self.colors = colors
        self.position = position  # Position will be a tuple (x, y, z) or another format

    def __repr__(self):
        return f"{self.__class__.__name__}({self.colors}, {self.position})"

    def set_position(self, position):
        """Update the position of the piece."""
        self.position = position

    def get_faces(self):
        """Return the face-color map."""
        return self.colors


class Center(Piece):
    def __init__(self, colors, position=None):
        # Center piece must have exactly 1 face and color
        if len(colors) != 1:
            raise ValueError("Center piece must have exactly 1 color and 1 face.")
        super().__init__(colors, position)


class Edge(Piece):
    def __init__(self, colors, position=None):
        # Edge piece must have exactly 2 faces and colors
        if len(colors) != 2:
            raise ValueError("Edge piece must have exactly 2 colors and 2 faces.")
        super().__init__(colors, position)  # Edge piece has a dictionary of two faces with their colors


class Corner(Piece):
    def __init__(self, colors, position=None):
        # Corner piece must have exactly 3 faces and colors
        if len(colors) != 3:
            raise ValueError("Corner piece must have exactly 3 colors and 3 faces.")
        super().__init__(colors, position)  # Corner piece has a dictionary of three faces with their colors
