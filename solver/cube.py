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

    # ------- Display Functions -------
    def display(self):
        """Display the cube in a 2D format."""

        U = self.get_face(Face.U)
        D = self.get_face(Face.D)
        F = self.get_face(Face.F)
        B = self.get_face(Face.B)
        R = self.get_face(Face.R)
        L = self.get_face(Face.L)

        # fmt: off
        def print_row(row):
            return "\t".join(row)

        print()
        for row in U:
            print("\t\t\t" + print_row(row))
        for i in range(3):
            print(print_row(L[i]) + "\t" + print_row(F[i]) + "\t" + print_row(R[i]) + "\t" + print_row(B[i]))
        for row in D:
            print("\t\t\t" + print_row(row))
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

    def get_face(self, face: Face):
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
    
    

    # -------- Helper Functions --------
    def _get_color(self, piece, face):
        """Fetch the color of a piece for a specific face."""
        if piece is None:
            return "BLACK"  # Return a blank space for empty positions
        for color, piece_face in piece.get_faces().items():
            if piece_face == face:
                return color.name  # Return the color name
        return "BLACK"  # Return a blank space if no matching face is found
    
    def _rebuild_matrix(self):
        """Rebuild the matrix from the pieces."""
        for piece in self.pieces.values():
            x, y, z = piece.get_position()
            self.matrix[x][y][z] = piece

    def _rearrange_pieces(self, keys: list[str]):
        values = [self.pieces[key] for key in keys]

        values.insert(0, values.pop())
        
        for key, value in zip(keys, values):
            self.pieces[key] = value

    def _fetch_components(self, pieces: list[str]) -> list[list]:
        """Fetch the components of the pieces in the cube."""
        positions = []
        faces = []
        names = []
        for piece in pieces:
            if piece not in self.pieces:
                raise ValueError(f"Piece {piece} not found in cube.")
            positions.append(self.pieces[piece].get_position())
            faces.append(self.pieces[piece].get_faces())
            names.append(self.pieces[piece].get_name())
        return [positions, faces, names]

    def _apply_components(self, pieces: list[str], components: list[list]):
        """Apply the positions to the pieces in the cube."""
        positions = components[0]
        faces = components[1]
        names = components[2]

        for piece, position, face, name in zip(pieces, positions, faces, names):
            self.pieces[piece].set_position(position)
            self.pieces[piece].set_faces(face)
            self.pieces[piece].set_name(name)

    def _rotate_components(self, components: list[list], f: str) -> list[list]:
        """Rotate the positions and faces in the specified direction."""
        positions = components[0]
        faces = components[1]
        names = components[2]

        if f not in ["U", "D", "F", "B", "R", "L"]:
            raise ValueError(
                "Invalid face, must be one of 'U', 'D', 'F', 'B', 'R', 'L'."
            )
        
        # Rotate positions
        names.append(names.pop(0))  # Rotate names clockwise
        positions.append(positions.pop(0))  # Rotate positions clockwise

        # Rotate faces
        for face_map in faces:
            rotated_faces = {}
            for color, face in face_map.items():
                if f == "U":
                    if face == Face.F:
                        rotated_faces[color] = Face.L
                    elif face == Face.L:
                        rotated_faces[color] = Face.B
                    elif face == Face.B:
                        rotated_faces[color] = Face.R
                    elif face == Face.R:
                        rotated_faces[color] = Face.F
                    else:
                        rotated_faces[color] = face
                elif f == "D":
                    if face == Face.F:
                        rotated_faces[color] = Face.R
                    elif face == Face.R:
                        rotated_faces[color] = Face.B
                    elif face == Face.B:
                        rotated_faces[color] = Face.L
                    elif face == Face.L:
                        rotated_faces[color] = Face.F
                    else:
                        rotated_faces[color] = face
                elif f == "R":
                    if face == Face.F:
                        rotated_faces[color] = Face.U
                    elif face == Face.U:
                        rotated_faces[color] = Face.B
                    elif face == Face.B:
                        rotated_faces[color] = Face.D
                    elif face == Face.D:
                        rotated_faces[color] = Face.F
                    else:
                        rotated_faces[color] = face
                elif f == "L":
                    if face == Face.F:
                        rotated_faces[color] = Face.D
                    elif face == Face.D:
                        rotated_faces[color] = Face.B
                    elif face == Face.B:
                        rotated_faces[color] = Face.U
                    elif face == Face.U:
                        rotated_faces[color] = Face.F
                    else:
                        rotated_faces[color] = face
                elif f == "B":
                    if face == Face.R:
                        rotated_faces[color] = Face.U
                    elif face == Face.U:
                        rotated_faces[color] = Face.L
                    elif face == Face.L:
                        rotated_faces[color] = Face.D
                    elif face == Face.D:
                        rotated_faces[color] = Face.R
                    else:
                        rotated_faces[color] = face
                elif f == "F":
                    if face == Face.R:
                        rotated_faces[color] = Face.D
                    elif face == Face.D:
                        rotated_faces[color] = Face.L
                    elif face == Face.L:
                        rotated_faces[color] = Face.U
                    elif face == Face.U:
                        rotated_faces[color] = Face.R
                    else:
                        rotated_faces[color] = face
            face_map.clear()
            face_map.update(rotated_faces)

        return [positions, faces, names]

    def _rotate_edges(self, edges: list[str], face: str):
        """Rotate the edge 3x3 grid in the specified direction."""
        # edges = [edge1, edge2, edge3, edge4] where each edge is a string like "UF", "UL", etc.
        components = self._fetch_components(edges)
        rotated_components = self._rotate_components(
            components, face
        )  # Rotate the positions to the right
        self._apply_components(edges, rotated_components)
        self._rearrange_pieces(edges)
        self._rebuild_matrix()
        

    def _rotate_corners(self, corners: list[str], face: str):
        """Rotate the corner 3x3 grid clockwise."""
        # corners = [corner1, corner2, corner3, corner4] where each corner is a string like "UFL", "UFR", etc.
        components = self._fetch_components(corners)
        rotated_components = self._rotate_components(
            components, face
        )  # Rotate the positions to the right
        self._apply_components(corners, rotated_components)
        self._rearrange_pieces(corners)
        self._rebuild_matrix()
        

    # -------- Rotation Functions --------
    def U(self):
        """Perform a U rotation (Up face clockwise)."""
        self._rotate_edges(["UF", "UL", "UB", "UR"], "U")
        self._rotate_corners(["UFL", "UBL", "UBR", "UFR"], "U")

    def D(self):
        """Perform a D rotation (Down face clockwise)."""
        self._rotate_edges(["DF", "DR", "DB", "DL"], "D")
        self._rotate_corners(["DFL", "DFR", "DBR", "DBL"], "D")

    def F(self):
        """Perform an F rotation (Front face clockwise)."""
        self._rotate_edges(["UF", "FR", "DF", "FL"], "F")
        self._rotate_corners(["UFL", "UFR", "DFR", "DFL"], "F")

    def B(self):
        """Perform a B rotation (Back face clockwise)."""
        self._rotate_edges(["UB", "BL", "DB", "BR"], "B")
        self._rotate_corners(["UBL", "DBL", "DBR", "UBR"], "B")

    def R(self):
        """Perform an R rotation (Right face clockwise)."""
        self._rotate_edges(["UR", "BR", "DR", "FR"], "R")
        self._rotate_corners(["UFR", "UBR", "DBR", "DFR"], "R")

    def L(self):
        """Perform an L rotation (Left face clockwise)."""
        self._rotate_edges(["UL", "FL", "DL", "BL"], "L")
        self._rotate_corners(["UFL", "DFL", "DBL", "UBL"], "L")
    
    def U_prime(self):
        """Perform a U' rotation (Up face clockwise)."""
        self.U()
        self.U()
        self.U()
    
    def D_prime(self):
        """Perform a D' rotation (Down face counter-clockwise)."""
        self.D()
        self.D()
        self.D()

    def F_prime(self):
        """Perform an F' rotation (Front face counter-clockwise)."""
        self.F()
        self.F()
        self.F()

    def B_prime(self):
        """Perform a B' rotation (Back face counter-clockwise)."""
        self.B()
        self.B()
        self.B()

    def R_prime(self):
        """Perform an R' rotation (Right face counter-clockwise)."""
        self.R()
        self.R()
        self.R()

    def L_prime(self):
        """Perform an L' rotation (Left face counter-clockwise)."""
        self.L()
        self.L()
        self.L()
