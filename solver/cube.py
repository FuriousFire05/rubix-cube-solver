# solver/cube.py

from solver.pieces import Center, Edge, Corner
from utils.faces import Face
from utils.colors import Color


class RubiksCube:
    def __init__(self):
        """Initialize a 3x3x3 Rubik's Cube."""

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
                ({Color.YELLOW: Face.U},  "U",  (1, 2, 1)),     # Up center
                ({Color.WHITE: Face.D},   "D",  (1, 0, 1)),     # Down center
                ({Color.BLUE: Face.F},    "F",  (1, 1, 2)),     # Front center
                ({Color.GREEN: Face.B},   "B",  (1, 1, 0)),     # Back center
                ({Color.RED: Face.R},     "R",  (2, 1, 1)),     # Right center
                ({Color.ORANGE: Face.L},  "L",  (0, 1, 1)),     # Left center
            ]),

            (Edge, [
                ({Color.YELLOW: Face.U, Color.BLUE: Face.F},    "UF",   (1, 2, 2)),     # Up-Front edge
                ({Color.YELLOW: Face.U, Color.ORANGE: Face.L},  "UL",   (0, 2, 1)),     # Up-Left edge
                ({Color.YELLOW: Face.U, Color.GREEN: Face.B},   "UB",   (1, 2, 0)),     # Up-Back edge
                ({Color.YELLOW: Face.U, Color.RED: Face.R},     "UR",   (2, 2, 1)),     # Up-Right edge

                ({Color.WHITE: Face.D,  Color.BLUE: Face.F},     "DF",   (1, 0, 2)),    # Down-Front edge
                ({Color.WHITE: Face.D,  Color.RED: Face.R},      "DR",   (2, 0, 1)),    # Down-Right edge
                ({Color.WHITE: Face.D,  Color.ORANGE: Face.L},   "DL",   (0, 0, 1)),    # Down-Left edge
                ({Color.WHITE: Face.D,  Color.GREEN: Face.B},    "DB",   (1, 0, 0)),    # Down-Back edge

                ({Color.BLUE: Face.F,   Color.ORANGE: Face.L},   "FL",   (0, 1, 2)),    # Front-Left edge
                ({Color.BLUE: Face.F,   Color.RED: Face.R},      "FR",   (2, 1, 2)),    # Front-Right edge
                ({Color.GREEN: Face.B,  Color.ORANGE: Face.L},   "BL",   (0, 1, 0)),    # Back-Left edge
                ({Color.GREEN: Face.B,  Color.RED: Face.R},      "BR",   (2, 1, 0)),    # Back-Right edge
            ]),

            (Corner, [
                ({Color.YELLOW: Face.U, Color.BLUE: Face.F,  Color.ORANGE: Face.L}, "UFL",  (0, 2, 2)),    # Up-Front-Left corner
                ({Color.YELLOW: Face.U, Color.BLUE: Face.F,  Color.RED: Face.R},    "UFR",  (2, 2, 2)),    # Up-Front-Right corner
                ({Color.YELLOW: Face.U, Color.GREEN: Face.B, Color.ORANGE: Face.L}, "UBL",  (0, 2, 0)),    # Up-Back-Left corner
                ({Color.YELLOW: Face.U, Color.GREEN: Face.B, Color.RED: Face.R},    "UBR",  (2, 2, 0)),    # Up-Back-Right corner

                ({Color.WHITE: Face.D,  Color.BLUE: Face.F,  Color.ORANGE: Face.L}, "DFL",  (0, 0, 2)),    # Down-Front-Left corner
                ({Color.WHITE: Face.D,  Color.BLUE: Face.F,  Color.RED: Face.R},    "DFR",  (2, 0, 2)),    # Down-Front-Right corner
                ({Color.WHITE: Face.D,  Color.GREEN: Face.B, Color.ORANGE: Face.L}, "DBL",  (0, 0, 0)),    # Down-Back-Left corner
                ({Color.WHITE: Face.D,  Color.GREEN: Face.B, Color.RED: Face.R},    "DBR",  (2, 0, 0)),    # Down-Back-Right corner
            ])
        ]

        # Creating Objects
        for piece_class, pieces in piece_definitions:
            for colors, name, (x, y, z) in pieces:
                self.matrix[x][y][z] = self.pieces[name] = piece_class(colors, name,  (x, y, z))
        # fmt: on

    # -------- Display Function --------
    def display(self):
        """Display the cube in a 2D format."""

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

    def _fetch_components(self, pieces: list[str]) -> list[list]:
        """Fetch the components of the pieces in the cube."""
        positions = []
        faces = []
        for piece in pieces:
            if piece not in self.pieces:
                raise ValueError(f"Piece {piece} not found in cube.")
            positions.append(self.pieces[piece].get_position())
            faces.append(self.pieces[piece].get_faces())
        print(f"Fetched positions: {positions}")
        print(f"Fetched faces: {faces}")
        return [positions, faces]

    def _apply_components(self, pieces: list[str], components: list[list]):
        """Apply the positions to the pieces in the cube."""
        positions, faces = components
        for piece, position, face in zip(pieces, positions, faces):
            print(f"Applying to piece {piece}: position={position}, faces={face}")
            self.pieces[piece].set_position(position)
            self.pieces[piece].set_faces(face)

    def _rotate_components(self, components: list[list], direction: str, f: str):
        """Rotate the positions and faces in the specified direction."""
        positions, faces = components

        if f not in ["U", "D", "F", "B", "R", "L"]:
            raise ValueError(
                "Invalid face, must be one of 'U', 'D', 'F', 'B', 'R', 'L'."
            )
        # Rotate positions
        if direction == "acw":
            positions.insert(0, positions.pop())  # Rotate positions counter-clockwise
        elif direction == "cw":
            positions.append(positions.pop(0))  # Rotate positions clockwise
        else:
            raise ValueError("Invalid Direction, must be 'cw' or 'acw'.")

        # Rotate faces
        for face_map in faces:
            rotated_faces = {}
            for color, face in face_map.items():
                if f in ["U", "D"]:
                    if direction == "cw":
                        # Counter-clockwise rotation of face mappings
                        if face == Face.F:
                            rotated_faces[color] = Face.L
                        elif face == Face.L:
                            rotated_faces[color] = Face.B
                        elif face == Face.B:
                            rotated_faces[color] = Face.R
                        elif face == Face.R:
                            rotated_faces[color] = Face.F
                        else:
                            rotated_faces[color] = face  # No change for other faces
                    else:
                        # Clockwise rotation of face mappings
                        if face == Face.F:
                            rotated_faces[color] = Face.R
                        elif face == Face.R:
                            rotated_faces[color] = Face.B
                        elif face == Face.B:
                            rotated_faces[color] = Face.L
                        elif face == Face.L:
                            rotated_faces[color] = Face.F
                        else:
                            rotated_faces[color] = face  # No change for other faces
                elif f in ["F", "B"]:
                    if direction == "cw":
                        # Clockwise rotation of face mappings
                        if face == Face.D:
                            rotated_faces[color] = Face.L
                        elif face == Face.L:
                            rotated_faces[color] = Face.U
                        elif face == Face.U:
                            rotated_faces[color] = Face.R
                        elif face == Face.R:
                            rotated_faces[color] = Face.D
                        else:
                            rotated_faces[color] = face  # No change for other faces
                    else:
                        # Counter-Clockwise rotation of face mappings
                        if face == Face.D:
                            rotated_faces[color] = Face.R
                        elif face == Face.R:
                            rotated_faces[color] = Face.U
                        elif face == Face.U:
                            rotated_faces[color] = Face.L
                        elif face == Face.L:
                            rotated_faces[color] = Face.D
                        else:
                            rotated_faces[color] = face  # No change for other faces
                else:
                    if direction == "cw":
                        # Clockwise rotation of face mappings
                        if face == Face.D:
                            rotated_faces[color] = Face.F
                        elif face == Face.F:
                            rotated_faces[color] = Face.U
                        elif face == Face.U:
                            rotated_faces[color] = Face.B
                        elif face == Face.B:
                            rotated_faces[color] = Face.D
                        else:
                            rotated_faces[color] = face  # No change for other faces
                    else:
                        # Counter-Clockwise rotation of face mappings
                        if face == Face.D:
                            rotated_faces[color] = Face.B
                        elif face == Face.B:
                            rotated_faces[color] = Face.U
                        elif face == Face.U:
                            rotated_faces[color] = Face.F
                        elif face == Face.F:
                            rotated_faces[color] = Face.D
                        else:
                            rotated_faces[color] = face  # No change for other faces
            face_map.clear()
            face_map.update(rotated_faces)

        return [positions, faces]

    def _rotate_edges(self, edges: list[str], direction: str, face: str):
        """Rotate the edge 3x3 grid in the specified direction."""
        # edges = [edge1, edge2, edge3, edge4] where each edge is a string like "UF", "UL", etc.
        print(f"Rotating edges: {edges} in direction {direction}")
        components = self._fetch_components(edges)
        components = self._rotate_components(
            components, direction, face
        )  # Rotate the positions to the right
        self._apply_components(edges, components)

    def _rotate_corners(self, corners: list[str], direction: str, face: str):
        """Rotate the corner 3x3 grid clockwise."""
        # corners = [corner1, corner2, corner3, corner4] where each corner is a string like "UFL", "UFR", etc.
        print(f"Rotating corners: {corners} in direction {direction}")
        components = self._fetch_components(corners)
        components = self._rotate_components(
            components, direction, face
        )  # Rotate the positions to the right
        self._apply_components(corners, components)

    def _get_face(self, face: Face):
        """Return a 3x3 array of color initials for the given face."""
        # Validate the face
        if type(face) is not Face:
            raise KeyError(f"Invalid face: {face}. Must be a Face Enum.")

        face_grid = [["" for _ in range(3)] for _ in range(3)]
        self._rebuild_matrix()  # Ensure the matrix is up to date

        if face == Face.U:
            y = 2
            for x in range(3):
                for z in range(3):
                    piece = self.matrix[x][y][z]
                    face_grid[z][x] = self._get_color(piece, face)

        elif face == Face.D:
            y = 0
            for x in range(3):
                for z in range(3):
                    piece = self.matrix[x][y][z]
                    face_grid[2 - z][x] = self._get_color(piece, face)

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
                    face_grid[2 - y][2 - x] = self._get_color(piece, face)

        elif face == Face.R:
            x = 2
            for y in range(3):
                for z in range(3):
                    piece = self.matrix[x][y][z]
                    face_grid[2 - y][2 - z] = self._get_color(piece, face)

        elif face == Face.L:
            x = 0
            for y in range(3):
                for z in range(3):
                    piece = self.matrix[x][y][z]
                    face_grid[2 - y][z] = self._get_color(piece, face)
        return face_grid

    def _get_color(self, piece, face):
        """Fetch the color of a piece for a specific face."""
        if piece is None:
            return " "  # Return a blank space for empty positions
        for color, piece_face in piece.get_faces().items():
            if piece_face == face:
                return color.name[0]  # Return the first letter of the color name
        return " "  # Return a blank space if no matching face is found

    # -------- Rotation Functions --------
    def U(self):
        """Perform a U rotation (Up face clockwise)."""
        self._rotate_edges(["UF", "UL", "UB", "UR"], "cw", "U")
        self._rotate_corners(["UFL", "UBL", "UBR", "UFR"], "cw", "U")

    def U_prime(self):
        """Perform a U' rotation (Up face clockwise)."""
        self._rotate_edges(["UF", "UL", "UB", "UR"], "acw", "U")
        self._rotate_corners(["UFL", "UBL", "UBR", "UFR"], "acw", "U")

    def D(self):
        """Perform a D rotation (Down face clockwise)."""
        self._rotate_edges(["DF", "DL", "DB", "DR"], "acw", "D")
        self._rotate_corners(["DFL", "DBL", "DBR", "DFR"], "acw", "D")

    def D_prime(self):
        """Perform a D' rotation (Down face counter-clockwise)."""
        self._rotate_edges(["DF", "DL", "DB", "DR"], "cw", "D")
        self._rotate_corners(["DFL", "DBL", "DBR", "DFR"], "cw", "D")

    def F(self):
        """Perform an F rotation (Front face clockwise)."""
        self._rotate_edges(["UF", "FR", "DF", "FL"], "cw", "F")
        self._rotate_corners(["UFL", "UFR", "DFR", "DFL"], "cw", "F")

    def F_prime(self):
        """Perform an F' rotation (Front face counter-clockwise)."""
        self._rotate_edges(["UF", "FR", "DF", "FL"], "acw", "F")
        self._rotate_corners(["UFL", "UFR", "DFR", "DFL"], "acw", "F")

    def B(self):
        """Perform a B rotation (Back face clockwise)."""
        self._rotate_edges(["UB", "BR", "DB", "BL"], "acw", "B")
        self._rotate_corners(["UBL", "UBR", "DBR", "DBL"], "acw", "B")

    def B_prime(self):
        """Perform a B' rotation (Back face counter-clockwise)."""
        self._rotate_edges(["UB", "BR", "DB", "BL"], "cw", "B")
        self._rotate_corners(["UBL", "UBR", "DBR", "DBL"], "cw", "B")

    def R(self):
        """Perform an R rotation (Right face clockwise)."""
        self._rotate_edges(["UR", "BR", "DR", "FR"], "cw", "R")
        self._rotate_corners(["UFR", "UBR", "DBR", "DFR"], "cw", "R")

    def R_prime(self):
        """Perform an R' rotation (Right face counter-clockwise)."""
        self._rotate_edges(["UR", "BR", "DR", "FR"], "acw", "R")
        self._rotate_corners(["UFR", "UBR", "DBR", "DFR"], "acw", "R")

    def L(self):
        """Perform an L rotation (Left face clockwise)."""
        self._rotate_edges(["UL", "BL", "DL", "FL"], "acw", "L")
        self._rotate_corners(["UFL", "UBL", "DBL", "DFL"], "acw", "L")

    def L_prime(self):
        """Perform an L' rotation (Left face counter-clockwise)."""
        self._rotate_edges(["UL", "BL", "DL", "FL"], "cw", "L")
        self._rotate_corners(["UFL", "UBL", "DBL", "DFL"], "cw", "L")
