# solver/pieces.py

class Piece:
    def __init__(self, color_face_map, position=None):
        # color_face_map will be a dictionary with face names as keys and the corresponding colors as values
        self.color_face_map = color_face_map
        self.position = position  # Position will be a tuple (x, y, z) or another format

    def __repr__(self):
        return f"{self.__class__.__name__}({self.color_face_map}, {self.position})"

    def set_position(self, position):
        """Update the position of the piece."""
        self.position = position

    def get_faces(self):
        """Return the face-color map."""
        return self.color_face_map


class Center(Piece):
    def __init__(self, color, face, position=None):
        # Centers are only associated with one face, so the dictionary will have a single key-value pair
        super().__init__({face: color}, position)  # For a center piece, only one face is involved


class Edge(Piece):
    def __init__(self, color_face_map, position=None):
        # Edge piece must have exactly 2 faces and colors
        if len(color_face_map) != 2:
            raise ValueError("Edge piece must have exactly 2 colors and 2 faces.")
        super().__init__(color_face_map, position)  # Edge piece has a dictionary of two faces with their colors


class Corner(Piece):
    def __init__(self, color_face_map, position=None):
        # Corner piece must have exactly 3 faces and colors
        if len(color_face_map) != 3:
            raise ValueError("Corner piece must have exactly 3 colors and 3 faces.")
        super().__init__(color_face_map, position)  # Corner piece has a dictionary of three faces with their colors
