# solver/cube.py

from solver.pieces import Center, Edge, Corner
from utils.faces import Face
from utils.colors import Color

class RubiksCube:
    def __init__(self):
        # List to hold all physical pieces (each piece is unique)
        self.pieces = []

        # Centralized position map: (Face, row, col) -> Piece
        self.positions = {}

        # Color scheme per face
        face_colors = {
            Face.U: Color.YELLOW,
            Face.D: Color.WHITE,
            Face.F: Color.BLUE,
            Face.B: Color.GREEN,
            Face.L: Color.ORANGE,
            Face.R: Color.RED,
        }

        # -------- Initialize Centers --------
        center_positions = {
            Face.U: (Face.U, 1, 1), # Up center
            Face.D: (Face.D, 1, 1), # Down center
            Face.F: (Face.F, 1, 1), # Front center
            Face.B: (Face.B, 1, 1), # Back center
            Face.L: (Face.L, 1, 1), # Left center
            Face.R: (Face.R, 1, 1), # Right center
        }

        for face, pos in center_positions.items():
            center = Center({face: face_colors[face]}, f"{face.name}C") # Create a center piece
            self.pieces.append(center)                                  # Add to pieces list
            self.positions[pos] = center                                # Map position to piece

        # -------- Initialize Edges --------
        edges = [
            ({Face.U: Color.YELLOW, Face.F: Color.BLUE}, "UF", (Face.U, 2, 1), (Face.F, 0, 1)),     # Up-Front edge
            ({Face.U: Color.YELLOW, Face.R: Color.RED}, "UR", (Face.U, 1, 2), (Face.R, 0, 1)),      # Up-Right edge
            ({Face.U: Color.YELLOW, Face.L: Color.ORANGE}, "UL", (Face.U, 1, 0), (Face.L, 0, 1)),   # Up-Left edge
            ({Face.U: Color.YELLOW, Face.B: Color.GREEN}, "UB", (Face.U, 0, 1), (Face.B, 0, 1)),    # Up-Back edge

            ({Face.D: Color.WHITE, Face.F: Color.BLUE}, "DF", (Face.D, 0, 1), (Face.F, 2, 1)),      # Down-Front edge
            ({Face.D: Color.WHITE, Face.R: Color.RED}, "DR", (Face.D, 1, 2), (Face.R, 2, 1)),       # Down-Right edge
            ({Face.D: Color.WHITE, Face.L: Color.ORANGE}, "DL", (Face.D, 1, 0), (Face.L, 2, 1)),    # Down-Left edge
            ({Face.D: Color.WHITE, Face.B: Color.GREEN}, "DB", (Face.D, 2, 1), (Face.B, 2, 1)),     # Down-Back edge

            ({Face.F: Color.BLUE, Face.L: Color.ORANGE}, "FL", (Face.F, 1, 0), (Face.L, 1, 2)),     # Front-Left edge
            ({Face.F: Color.BLUE, Face.R: Color.RED}, "FR", (Face.F, 1, 2), (Face.R, 1, 0)),        # Front-Right edge
            ({Face.B: Color.GREEN, Face.L: Color.ORANGE}, "BL", (Face.B, 1, 0), (Face.L, 1, 0)),    # Back-Left edge
            ({Face.B: Color.GREEN, Face.R: Color.RED}, "BR", (Face.B, 1, 2), (Face.R, 1, 2)),       # Back-Right edge
        ]

        for color_map, name, pos1, pos2 in edges:
            edge = Edge(color_map, name)    # Create an edge piece
            self.pieces.append(edge)        # Add to pieces list
            self.positions[pos1] = edge     # Map position 1 to piece
            self.positions[pos2] = edge     # Map position 2 to piece

        # -------- Initialize Corners --------
        corners = [
            ({Face.U: Color.YELLOW, Face.F: Color.BLUE, Face.L: Color.ORANGE}, "UFL", (Face.U, 2, 0), (Face.F, 0, 0), (Face.L, 0, 2)),  # Up-Front-Left corner
            ({Face.U: Color.YELLOW, Face.F: Color.BLUE, Face.R: Color.RED}, "UFR", (Face.U, 2, 2), (Face.F, 0, 2), (Face.R, 0, 0)),     # Up-Front-Right corner
            ({Face.U: Color.YELLOW, Face.B: Color.GREEN, Face.L: Color.ORANGE}, "UBL", (Face.U, 0, 0), (Face.B, 0, 2), (Face.L, 0, 0)), # Up-Back-Left corner
            ({Face.U: Color.YELLOW, Face.B: Color.GREEN, Face.R: Color.RED}, "UBR", (Face.U, 0, 2), (Face.B, 0, 0), (Face.R, 0, 2)),    # Up-Back-Right corner

            ({Face.D: Color.WHITE, Face.F: Color.BLUE, Face.L: Color.ORANGE}, "DFL", (Face.D, 0, 0), (Face.F, 2, 0), (Face.L, 2, 2)),   # Down-Front-Left corner
            ({Face.D: Color.WHITE, Face.F: Color.BLUE, Face.R: Color.RED}, "DFR", (Face.D, 0, 2), (Face.F, 2, 2), (Face.R, 2, 0)),      # Down-Front-Right corner
            ({Face.D: Color.WHITE, Face.B: Color.GREEN, Face.L: Color.ORANGE}, "DBL", (Face.D, 2, 0), (Face.B, 2, 2), (Face.L, 2, 0)),  # Down-Back-Left corner
            ({Face.D: Color.WHITE, Face.B: Color.GREEN, Face.R: Color.RED}, "DBR", (Face.D, 2, 2), (Face.B, 2, 0), (Face.R, 2, 2)),     # Down-Back-Right corner
        ]

        for color_map, name, pos1, pos2, pos3 in corners:
            corner = Corner(color_map, name)    # Create a corner piece
            self.pieces.append(corner)          # Add to pieces list
            self.positions[pos1] = corner       # Map position 1 to piece
            self.positions[pos2] = corner       # Map position 2 to piece
            self.positions[pos3] = corner       # Map position 3 to piece


    """*************************************************************************************************************************************************************"""


    # -------- Display Function --------
    def display(self):
        # 3x3 grid for each face
        """
        {
            Face.U: [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
            Face.D: [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
            Face.F: ...
            ...
        }
        """
        face_grids = {face: [[" " for _ in range(3)] for _ in range(3)] for face in Face}

        for (face, row, col), piece in self.positions.items():
            color = piece.colors.get(face)
            if color:
                face_grids[face][row][col] = color.name[0]  # Just first letter of color

        # Print each face in order
        for face in Face:
            print(f"{face.name} Face:")
            for row in face_grids[face]:
                print(" ".join(row))
            print()


    """*************************************************************************************************************************************************************"""

    # -------- Helper Functions(CW, ACW) --------
    def _rotate_face_cw(self, face: Face):
        """Rotate the face 3x3 grid clockwise."""
        new_positions = {}
        for row in range(3):
            for col in range(3):
                old_pos = (face, row, col)
                new_row, new_col = col, 2 - row  # Clockwise mapping
                new_positions[(face, new_row, new_col)] = self.positions[old_pos]
        self.positions.update(new_positions)

    def _rotate_face_acw(self, face: Face):
        """Rotate the face 3x3 grid anti-clockwise."""
        new_positions = {}
        for row in range(3):
            for col in range(3):
                old_pos = (face, row, col)
                new_row, new_col = 2 - col, row  # Anti-clockwise mapping
                new_positions[(face, new_row, new_col)] = self.positions[old_pos]
        self.positions.update(new_positions)

    def _rotate_edge_cw(self, pos1, pos2, pos3, pos4):
        """Rotate edge positions clockwise."""
        temp1 = self.positions[pos1]
        temp2 = self.positions[pos2]
        temp3 = self.positions[pos3]
        temp4 = self.positions[pos4]
        self.positions[pos2] = temp1
        self.positions[pos3] = temp2
        self.positions[pos4] = temp3
        self.positions[pos1] = temp4
    
    def _rotate_edge_acw(self, pos1, pos2, pos3, pos4):
        """Rotate edge positions anti-clockwise."""
        temp1 = self.positions[pos1]
        temp2 = self.positions[pos2]
        temp3 = self.positions[pos3]
        temp4 = self.positions[pos4]
        self.positions[pos4] = temp3
        self.positions[pos3] = temp2
        self.positions[pos2] = temp1
        self.positions[pos1] = temp4

    def _rotate_corner_cw(self, pos1, pos2, pos3, pos4):
        """Rotate corner positions clockwise."""
        temp1 = self.positions[pos1]
        temp2 = self.positions[pos2]
        temp3 = self.positions[pos3]
        temp4 = self.positions[pos4]
        self.positions[pos2] = temp1
        self.positions[pos3] = temp2
        self.positions[pos4] = temp3
        self.positions[pos1] = temp4

    def _rotate_corner_acw(self, pos1, pos2, pos3, pos4):
        """Rotate corner positions anti-clockwise."""
        temp1 = self.positions[pos1]
        temp2 = self.positions[pos2]
        temp3 = self.positions[pos3]
        temp4 = self.positions[pos4]
        self.positions[pos4] = temp1
        self.positions[pos3] = temp4
        self.positions[pos2] = temp3
        self.positions[pos1] = temp2

    
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