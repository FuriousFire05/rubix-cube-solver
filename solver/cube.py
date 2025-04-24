# solver/cube.py

from solver.pieces import Center, Edge, Corner
from utils.faces import Face
from utils.colors import Color

class RubiksCube:
    def __init__(self):
        # Initialize the pieces for the Rubik's Cube with correct face orientations.
        # The cube has 6 faces, each with its own color.
        # Each face will have a list of pieces (centers, edges, corners).

        # Center pieces are unique to each face and are not shared with other faces.
        # Center pieces
        self.faces = {
            Face.U: [Center({Face.U: Color.YELLOW}, "U1")],  # Center piece for Up face at position U1
            Face.D: [Center({Face.D: Color.WHITE}, "D1")],   # Center piece for Down face at position D1
            Face.F: [Center({Face.F: Color.BLUE}, "F1")],    # Center piece for Front face at position F1
            Face.B: [Center({Face.B: Color.GREEN}, "B1")],   # Center piece for Back face at position B1
            Face.L: [Center({Face.L: Color.ORANGE}, "L1")],  # Center piece for Left face at position L1
            Face.R: [Center({Face.R: Color.RED}, "R1")],     # Center piece for Right face at position R1
        }

        # Edge and corner pieces will be shared between faces (2 for edges, 3 for corners).
        # Edge pieces
        self.faces[Face.U].extend([
            Edge({Face.U: Color.YELLOW, Face.F: Color.BLUE}, "U2"),   # Up-Front edge at position U2
            Edge({Face.U: Color.YELLOW, Face.R: Color.RED}, "U3"),    # Up-Right edge at position U3
            Edge({Face.U: Color.YELLOW, Face.L: Color.ORANGE}, "U4"), # Up-Left edge at position U4
            Edge({Face.U: Color.YELLOW, Face.B: Color.GREEN}, "U5"),  # Up-Back edge at position U5
        ])
        self.faces[Face.D].extend([
            Edge({Face.D: Color.WHITE, Face.F: Color.BLUE}, "D2"),    # Down-Front edge at position D2
            Edge({Face.D: Color.WHITE, Face.R: Color.RED}, "D3"),     # Down-Right edge at position D3
            Edge({Face.D: Color.WHITE, Face.L: Color.ORANGE}, "D4"),  # Down-Left edge at position D4
            Edge({Face.D: Color.WHITE, Face.B: Color.GREEN}, "D5"),   # Down-Back edge at position D5
        ])
        self.faces[Face.F].extend([
            Edge({Face.F: Color.BLUE, Face.U: Color.YELLOW}, "F2"),   # Front-Up edge at position F2
            Edge({Face.F: Color.BLUE, Face.D: Color.WHITE}, "F3"),    # Front-Down edge at position F3
            Edge({Face.F: Color.BLUE, Face.L: Color.ORANGE}, "F4"),   # Front-Left edge at position F4
            Edge({Face.F: Color.BLUE, Face.R: Color.RED}, "F5"),      # Front-Right edge at position F5
        ])
        self.faces[Face.B].extend([
            Edge({Face.B: Color.GREEN, Face.U: Color.YELLOW}, "B2"),  # Back-Up edge at position B2
            Edge({Face.B: Color.GREEN, Face.D: Color.WHITE}, "B3"),   # Back-Down edge at position B3
            Edge({Face.B: Color.GREEN, Face.L: Color.ORANGE}, "B4"),  # Back-Left edge at position B4
            Edge({Face.B: Color.GREEN, Face.R: Color.RED}, "B5"),     # Back-Right edge at position B5
        ])

        # Corner pieces
        self.faces[Face.U].extend([
            Corner({Face.U: Color.YELLOW, Face.F: Color.BLUE, Face.L: Color.ORANGE}, "U6"),  # Up-Front-Left corner at position U6
            Corner({Face.U: Color.YELLOW, Face.F: Color.BLUE, Face.R: Color.RED}, "U7"),   # Up-Front-Right corner at position U7
        ])
        self.faces[Face.D].extend([
            Corner({Face.D: Color.WHITE, Face.F: Color.BLUE, Face.L: Color.ORANGE}, "D6"),    # Down-Front-Left corner at position D6
            Corner({Face.D: Color.WHITE, Face.F: Color.BLUE, Face.R: Color.RED}, "D7"),       # Down-Front-Right corner at position D7
        ])
        self.faces[Face.F].extend([
            Corner({Face.F: Color.BLUE, Face.U: Color.YELLOW, Face.L: Color.ORANGE}, "F6"),   # Front-Up-Left corner at position F6
            Corner({Face.F: Color.BLUE, Face.U: Color.YELLOW, Face.R: Color.RED}, "F7"),      # Front-Up-Right corner at position F7
            Corner({Face.F: Color.BLUE, Face.D: Color.WHITE, Face.L: Color.ORANGE}, "F8"),    # Front-Down-Left corner at position F8
            Corner({Face.F: Color.BLUE, Face.D: Color.WHITE, Face.R: Color.RED}, "F9"),       # Front-Down-Right corner at position F9
        ])
        self.faces[Face.B].extend([
            Corner({Face.B: Color.GREEN, Face.U: Color.YELLOW, Face.L: Color.ORANGE}, "B6"),  # Back-Up-Left corner at position B6
            Corner({Face.B: Color.GREEN, Face.U: Color.YELLOW, Face.R: Color.RED}, "B7"),     # Back-Up-Right corner at position B7
            Corner({Face.B: Color.GREEN, Face.D: Color.WHITE, Face.L: Color.ORANGE}, "B8"),   # Back-Down-Left corner at position B8
            Corner({Face.B: Color.GREEN, Face.D: Color.WHITE, Face.R: Color.RED}, "B9"),      # Back-Down-Right corner at position B9
        ])
        self.faces[Face.L].extend([
            Corner({Face.L: Color.ORANGE, Face.U: Color.YELLOW, Face.F: Color.BLUE}, "L6"),   # Left-Up-Front corner at position L6
            Corner({Face.L: Color.ORANGE, Face.D: Color.WHITE, Face.F: Color.BLUE}, "L7"),    # Left-Down-Front corner at position L7
        ])
        self.faces[Face.R].extend([
            Corner({Face.R: Color.RED, Face.U: Color.YELLOW, Face.F: Color.BLUE}, "R6"),      # Right-Up-Front corner at position R6
            Corner({Face.R: Color.RED, Face.D: Color.WHITE, Face.F: Color.BLUE}, "R7"),       # Right-Down-Front corner at position R7
        ])

    def display(self):
        """Display the current state of the cube"""
        for face, pieces in self.faces.items():
            print(f"{face} face:")
            for piece in pieces:
                print(f"  {piece}")
            print()

    def U(self):
        """Perform a U rotation (Up face clockwise)."""
        # Update the positions of the pieces based on the U rotation
        # This will affect the pieces on the U, F, B, and D faces.
        pass

    def U_prime(self):
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