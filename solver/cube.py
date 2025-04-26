# solver/cube.py

from solver.pieces import Center, Edge, Corner
from utils.faces import Face
from utils.colors import Color

class RubiksCube:
    def __init__(self):
        # Dictionary to hold all physical pieces (each piece is unique)
        self.pieces = {}

        # List to hold the pieces in the cube in a 3D grid
        self.matrix = [[[None for _ in range(3)] for _ in range(3)] for _ in range(3)]

        # Color scheme
        # Up: Yellow
        # Down: White 
        # Front: Blue 
        # Back: Green
        # Right: Red
        # Left: Orange

        # Initializing Pieces
        centers = [
            ({Face.U: Color.YELLOW},  "U",  (1, 2, 1)),     # Up center
            ({Face.D: Color.WHITE},   "D",  (1, 0, 1)),     # Down center
            ({Face.F: Color.BLUE},    "F",  (1, 1, 2)),     # Front center
            ({Face.B: Color.GREEN},   "B",  (1, 1, 0)),     # Back center
            ({Face.R: Color.RED},     "R",  (2, 1, 1)),     # Right center
            ({Face.L: Color.ORANGE},  "L",  (0, 1, 1)),     # Left center
        ]

        edges = [
            ({Face.U: Color.YELLOW, Face.F: Color.BLUE},    "UF",   (1, 2, 2)),    # Up-Front edge
            ({Face.U: Color.YELLOW, Face.R: Color.RED},     "UR",   (2, 2, 1)),    # Up-Right edge
            ({Face.U: Color.YELLOW, Face.L: Color.ORANGE},  "UL",   (0, 2, 1)),    # Up-Left edge
            ({Face.U: Color.YELLOW, Face.B: Color.GREEN},   "UB",   (1, 2, 0)),    # Up-Back edge

            ({Face.D: Color.WHITE,  Face.F: Color.BLUE},     "DF",   (1, 0, 2)),    # Down-Front edge
            ({Face.D: Color.WHITE,  Face.R: Color.RED},      "DR",   (2, 0, 1)),    # Down-Right edge
            ({Face.D: Color.WHITE,  Face.L: Color.ORANGE},   "DL",   (0, 0, 1)),    # Down-Left edge
            ({Face.D: Color.WHITE,  Face.B: Color.GREEN},    "DB",   (1, 0, 0)),    # Down-Back edge

            ({Face.F: Color.BLUE,   Face.L: Color.ORANGE},   "FL",   (0, 1, 2)),    # Front-Left edge
            ({Face.F: Color.BLUE,   Face.R: Color.RED},      "FR",   (2, 1, 2)),    # Front-Right edge
            ({Face.B: Color.GREEN,  Face.L: Color.ORANGE},   "BL",   (0, 1, 0)),    # Back-Left edge
            ({Face.B: Color.GREEN,  Face.R: Color.RED},      "BR",   (2, 1, 0)),    # Back-Right edge
        ]

        corners = [
            ({Face.U: Color.YELLOW, Face.F: Color.BLUE,  Face.L: Color.ORANGE}, "UFL",  (0, 2, 2)),    # Up-Front-Left corner
            ({Face.U: Color.YELLOW, Face.F: Color.BLUE,  Face.R: Color.RED},    "UFR",  (2, 2, 2)),    # Up-Front-Right corner
            ({Face.U: Color.YELLOW, Face.B: Color.GREEN, Face.L: Color.ORANGE}, "UBL",  (0, 2, 0)),    # Up-Back-Left corner
            ({Face.U: Color.YELLOW, Face.B: Color.GREEN, Face.R: Color.RED},    "UBR",  (2, 2, 0)),    # Up-Back-Right corner

            ({Face.D: Color.WHITE,  Face.F: Color.BLUE,  Face.L: Color.ORANGE}, "DFL",  (0, 0, 2)),    # Down-Front-Left corner
            ({Face.D: Color.WHITE,  Face.F: Color.BLUE,  Face.R: Color.RED},    "DFR",  (2, 0, 2)),    # Down-Front-Right corner
            ({Face.D: Color.WHITE,  Face.B: Color.GREEN, Face.L: Color.ORANGE}, "DBL",  (0, 0, 0)),    # Down-Back-Left corner
            ({Face.D: Color.WHITE,  Face.B: Color.GREEN, Face.R: Color.RED},    "DBR",  (2, 0, 0)),    # Down-Back-Right corner
        ]

        # Creating Objects
        for colors, name, position in centers:
            piece = Center(colors, position)
            self.pieces[name] = piece
            self.matrix[position[0]][position[1]][position[2]] = piece

        for colors, name, position in edges:
            piece = Edge(colors, position)
            self.pieces[name] = piece
            self.matrix[position[0]][position[1]][position[2]] = piece

        for colors, name, position in corners:
            piece = Corner(colors, position)
            self.pieces[name] = piece
            self.matrix[position[0]][position[1]][position[2]] = piece

    # -------- Display Function --------
    def display(self):
        pass

    # -------- Helper Functions(CW, ACW) --------
    def _rotate_face_cw(self, face: Face):
        """Rotate the face 3x3 grid clockwise."""
        pass

    def _rotate_face_acw(self, face: Face):
        """Rotate the face 3x3 grid anti-clockwise."""
        pass

    def _get_row(self, face: Face, row: int):
        """Return a row from a face."""
        pass

    def _set_row(self, face: Face, row: int, values):
        """Set a row on a face."""
        pass

    # -------- Rotation Functions --------
    def U(self):
        """Perform a U rotation (Up face clockwise)."""
        pass

    def U_prime(self):
        """Perform a U rotation (Up face clockwise)."""
        pass

    def D(self):
        """Perform a U rotation (Up face clockwise)."""
        pass

    def D_prime(self):
        """Perform a U' rotation (Up face counter-clockwise)."""
        pass

    def F(self):
        """Perform an F rotation (Front face clockwise)."""
        pass

    def F_prime(self):
        """Perform an F' rotation (Front face counter-clockwise)."""
        pass

    def B(self):
        """Perform a B rotation (Back face clockwise)."""
        pass

    def B_prime(self):
        """Perform a B' rotation (Back face counter-clockwise)."""
        pass

    def L(self):
        """Perform an L rotation (Left face clockwise)."""
        pass

    def L_prime(self):
        """Perform an L' rotation (Left face counter-clockwise)."""
        pass

    def R(self):
        """Perform an R rotation (Right face clockwise)."""
        pass

    def R_prime(self):
        """Perform an R' rotation (Right face counter-clockwise)."""
        pass