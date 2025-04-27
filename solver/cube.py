# solver/cube.py

from solver.pieces import Center, Edge, Corner
from utils.faces import Face
from utils.colors import Color


class RubiksCube:
    def __init__(self):
        """Initialize a 3x3x3 Rubik's Cube.""" ""
        # Dictionary to hold all physical pieces (each piece is unique)
        self.pieces = {}

        # List to hold the pieces in the cube in a 3D grid
        self.matrix = [[[None for _ in range(3)] for _ in range(3)] for _ in range(3)]

        # Color definitions for each face
        # UP: YELLOW, DOWN: WHITE, FRONT: BLUE, BACK: GREEN, RIGHT: RED, LEFT: ORANGE

        # Initializing Pieces
        # fmt: off
        piece_definitions = [
            (Center, [
                ({Face.U: Color.YELLOW},  "U",  (1, 2, 1)),     # Up center
                ({Face.D: Color.WHITE},   "D",  (1, 0, 1)),     # Down center
                ({Face.F: Color.BLUE},    "F",  (1, 1, 2)),     # Front center
                ({Face.B: Color.GREEN},   "B",  (1, 1, 0)),     # Back center
                ({Face.R: Color.RED},     "R",  (2, 1, 1)),     # Right center
                ({Face.L: Color.ORANGE},  "L",  (0, 1, 1)),     # Left center
            ]),

            (Edge, [
                ({Face.U: Color.YELLOW, Face.F: Color.BLUE},    "UF",   (1, 2, 2)),     # Up-Front edge
                ({Face.U: Color.YELLOW, Face.L: Color.ORANGE},  "UL",   (0, 2, 1)),     # Up-Left edge
                ({Face.U: Color.YELLOW, Face.B: Color.GREEN},   "UB",   (1, 2, 0)),     # Up-Back edge
                ({Face.U: Color.YELLOW, Face.R: Color.RED},     "UR",   (2, 2, 1)),     # Up-Right edge

                ({Face.D: Color.WHITE,  Face.F: Color.BLUE},     "DF",   (1, 0, 2)),    # Down-Front edge
                ({Face.D: Color.WHITE,  Face.R: Color.RED},      "DR",   (2, 0, 1)),    # Down-Right edge
                ({Face.D: Color.WHITE,  Face.L: Color.ORANGE},   "DL",   (0, 0, 1)),    # Down-Left edge
                ({Face.D: Color.WHITE,  Face.B: Color.GREEN},    "DB",   (1, 0, 0)),    # Down-Back edge

                ({Face.F: Color.BLUE,   Face.L: Color.ORANGE},   "FL",   (0, 1, 2)),    # Front-Left edge
                ({Face.F: Color.BLUE,   Face.R: Color.RED},      "FR",   (2, 1, 2)),    # Front-Right edge
                ({Face.B: Color.GREEN,  Face.L: Color.ORANGE},   "BL",   (0, 1, 0)),    # Back-Left edge
                ({Face.B: Color.GREEN,  Face.R: Color.RED},      "BR",   (2, 1, 0)),    # Back-Right edge
            ]),

            (Corner, [
                ({Face.U: Color.YELLOW, Face.F: Color.BLUE,  Face.L: Color.ORANGE}, "UFL",  (0, 2, 2)),    # Up-Front-Left corner
                ({Face.U: Color.YELLOW, Face.F: Color.BLUE,  Face.R: Color.RED},    "UFR",  (2, 2, 2)),    # Up-Front-Right corner
                ({Face.U: Color.YELLOW, Face.B: Color.GREEN, Face.L: Color.ORANGE}, "UBL",  (0, 2, 0)),    # Up-Back-Left corner
                ({Face.U: Color.YELLOW, Face.B: Color.GREEN, Face.R: Color.RED},    "UBR",  (2, 2, 0)),    # Up-Back-Right corner

                ({Face.D: Color.WHITE,  Face.F: Color.BLUE,  Face.L: Color.ORANGE}, "DFL",  (0, 0, 2)),    # Down-Front-Left corner
                ({Face.D: Color.WHITE,  Face.F: Color.BLUE,  Face.R: Color.RED},    "DFR",  (2, 0, 2)),    # Down-Front-Right corner
                ({Face.D: Color.WHITE,  Face.B: Color.GREEN, Face.L: Color.ORANGE}, "DBL",  (0, 0, 0)),    # Down-Back-Left corner
                ({Face.D: Color.WHITE,  Face.B: Color.GREEN, Face.R: Color.RED},    "DBR",  (2, 0, 0)),    # Down-Back-Right corner
            ])
        ]

        # Creating Objects
        for piece_class, pieces in piece_definitions:
            for colors, name, (x, y, z) in pieces:
                self.matrix[x][y][z] = self.pieces[name] = piece_class(colors, name,  (x, y, z))
        # fmt: on

    # -------- Display Function --------
    def display(self):
        U = self._get_face(Face.U)
        D = self._get_face(Face.D)
        F = self._get_face(Face.F)
        B = self._get_face(Face.B)
        R = self._get_face(Face.R)
        L = self._get_face(Face.L)

        # fmt: off
        def print_row(row):
            return " ".join(row)

        print()
        for row in U:
            print("      " + print_row(row))
        for i in range(3):
            print(print_row(L[i]) + " " + print_row(F[i]) + " " + print_row(R[i]) + " " + print_row(B[i]))
        for row in D:
            print("      " + print_row(row))
        print()
        # fmt: on

    def print_matrix(self):
        """Convert the cube matrix to a string representation."""

        self._rebuild_matrix()

        for y in [2, 1, 0]:
            for z in range(3):
                for x in range(3):
                    piece = self.matrix[x][y][z]
                    if piece is not None:
                        print(f"{piece.name}\t", end=" ")
                    else:
                        print(" \t", end=" ")
                print()
            print("\n")

    # -------- Helper Functions --------
    def _rebuild_matrix(self):
        """Rebuild the matrix from the pieces."""
        for piece in self.pieces.values():
            x, y, z = piece.get_position()
            self.matrix[x][y][z] = piece

    def _fetch_positions(self, pieces: list[str]) -> list[tuple[int, int, int]]:
        """Fetch the positions of the pieces in the cube."""
        positions = []
        for piece in pieces:
            if piece not in self.pieces:
                raise ValueError(f"Piece {piece} not found in cube.")
            positions.append(self.pieces[piece].get_position())
        return positions

    def _apply_positions(
        self, pieces: list[str], positions: list[tuple[int, int, int]]
    ):
        """Apply the positions to the pieces in the cube."""
        for piece, position in zip(pieces, positions):
            self.pieces[piece].set_position(position)

    def _rotate_positions(self, positions: list[tuple[int, int, int]], direction: str):
        """Rotate the positions in the specified direction."""
        if direction == "acw":
            return [positions[-1]] + positions[:-1]  # Rotate right
        elif direction == "cw":
            return positions[1:] + [positions[0]]  # Rotate left
        else:
            raise ValueError("Invalid Direction, must be 'cw' or 'acw'.")

    def _rotate_edges(self, edges: list[str], direction: str):
        """Rotate the edge 3x3 grid in the specified direction."""
        # edges = [edge1, edge2, edge3, edge4] where each edge is a string like "UF", "UL", etc.
        positions = self._fetch_positions(edges)
        positions = self._rotate_positions(
            positions, direction
        )  # Rotate the positions to the right
        self._apply_positions(edges, positions)

    def _rotate_corners(self, corners: list[str], direction: str):
        """Rotate the corner 3x3 grid clockwise."""
        # corners = [corner1, corner2, corner3, corner4] where each corner is a string like "UFL", "UFR", etc.
        positions = self._fetch_positions(corners)
        positions = self._rotate_positions(
            positions, direction
        )  # Rotate the positions to the right
        self._apply_positions(corners, positions)

    def _get_face(self, face: Face):
        """Return a 3x3 array of color initials for the given face."""
        # Validate the face
        if type(face) != Face:
            raise KeyError(f"Invalid face: {face}. Must be a Face Enum.")

        face_grid = [["" for _ in range(3)] for _ in range(3)]
        self._rebuild_matrix()  # Ensure the matrix is up to date

        if face == Face.U:
            y = 2
            for x in range(3):
                for z in range(3):
                    piece = self.matrix[x][y][z]
                    face_grid[2 - z][x] = self._get_color(piece, face)

        elif face == Face.D:
            y = 0
            for x in range(3):
                for z in range(3):
                    piece = self.matrix[x][y][z]
                    face_grid[z][x] = self._get_color(piece, face)

        elif face == Face.F:
            z = 2
            for x in range(3):
                for y in range(3):
                    piece = self.matrix[x][y][z]
                    face_grid[2 - y][x] = self._get_color(piece, face)

        elif face == Face.B:
            z = 0
            for x in range(3):
                for y in range(3):
                    piece = self.matrix[x][y][z]
                    face_grid[y][2 - x] = self._get_color(piece, face)

        elif face == Face.R:
            x = 2
            for y in range(3):
                for z in range(3):
                    piece = self.matrix[x][y][z]
                    face_grid[2 - y][z] = self._get_color(piece, face)

        elif face == Face.L:
            x = 0
            for y in range(3):
                for z in range(3):
                    piece = self.matrix[x][y][z]
                    face_grid[2 - y][2 - z] = self._get_color(piece, face)
        return face_grid

    def _get_color(self, piece, face):
        """Helper to get color initial for a given face."""
        if face in piece.colors:
            return piece.colors[face].name[0]  # like 'Y', 'B', etc.
        return " "  # Empty if no color on that face (e.g., centers, edges)

    # -------- Rotation Functions --------
    def U(self):
        """Perform a U rotation (Up face clockwise)."""
        self._rotate_edges(["UF", "UL", "UB", "UR"], "cw")
        self._rotate_corners(["UFL", "UBL", "UBR", "UFR"], "cw")

    def U_prime(self):
        """Perform a U' rotation (Up face clockwise)."""
        self._rotate_edges(["UF", "UL", "UB", "UR"], "acw")
        self._rotate_corners(["UFL", "UBL", "UBR", "UFR"], "acw")

    def D(self):
        """Perform a D rotation (Up face clockwise)."""
        self._rotate_edges(["DF", "DL", "DB", "DR"], "cw")
        self._rotate_corners(["DFL", "DFR", "DBR", "DBL"], "cw")

    def D_prime(self):
        """Perform a D' rotation (Up face counter-clockwise)."""
        self._rotate_edges(["DF", "DL", "DB", "DR"], "acw")
        self._rotate_corners(["DFL", "DFR", "DBR", "DBL"], "acw")

    def F(self):
        """Perform an F rotation (Front face clockwise)."""
        self._rotate_edges(["UF", "FR", "DF", "FL"], "cw")
        self._rotate_corners(["UFL", "UFR", "DFR", "DFL"], "cw")

    def F_prime(self):
        """Perform an F' rotation (Front face counter-clockwise)."""
        self._rotate_edges(["UF", "FR", "DF", "FL"], "acw")
        self._rotate_corners(["UFL", "UFR", "DFR", "DFL"], "acw")

    def B(self):
        """Perform a B rotation (Back face clockwise)."""
        self._rotate_edges(["UB", "BL", "DB", "BR"], "cw")
        self._rotate_corners(["UBL", "DBL", "DBR", "UBR"], "cw")

    def B_prime(self):
        """Perform a B' rotation (Back face counter-clockwise)."""
        self._rotate_edges(["UB", "BL", "DB", "BR"], "acw")
        self._rotate_corners(["UBL", "DBL", "DBR", "UBR"], "acw")

    def L(self):
        """Perform an L rotation (Left face clockwise)."""
        self._rotate_edges(["UL", "FL", "DL", "BL"], "cw")
        self._rotate_corners(["UFL", "DFL", "DBL", "UBL"], "cw")

    def L_prime(self):
        """Perform an L' rotation (Left face counter-clockwise)."""
        self._rotate_edges(["UL", "BL", "DL", "FL"], "acw")
        self._rotate_corners(["UFL", "UBL", "DBL", "DFL"], "acw")

    def R(self):
        """Perform an R rotation (Right face clockwise)."""
        self._rotate_edges(["UR", "BR", "DR", "FR"], "cw")
        self._rotate_corners(["UFR", "UBR", "DBR", "DFR"], "cw")

    def R_prime(self):
        """Perform an R' rotation (Right face counter-clockwise)."""
        self._rotate_edges(["UR", "BR", "DR", "FR"], "acw")
        self._rotate_corners(["UFR", "UBR", "DBR", "DFR"], "acw")
