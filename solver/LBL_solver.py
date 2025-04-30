# solver/LBL_solver.py

from core.cube import RubiksCube

class LBL_Solver:
    def __init__(self, cube):
        self.cube = cube
        self.moves = []  # Track the moves performed during solving

    
    def _apply_move(self, move):
        """
        Calls the appropriate move function on the cube and stores the move.
        """
        move_func = {
            "U": self.cube.U,
            "U'": self.cube.U_prime,
            "U2": self.cube.U2,
            "D": self.cube.D,
            "D'": self.cube.D_prime,
            "D2": self.cube.D2,
            "F": self.cube.F,
            "F'": self.cube.F_prime,
            "F2": self.cube.F2,
            "B": self.cube.B,
            "B'": self.cube.B_prime,
            "B2": self.cube.B2,
            "R": self.cube.R,
            "R'": self.cube.R_prime,
            "R2": self.cube.R2,
            "L": self.cube.L,
            "L'": self.cube.L_prime,
            "L2": self.cube.L2,
        }

        if move in move_func:
            move_func[move]()
            self.moves.append(move)

    def solve_white_cross(self):
        """
        Step 1 of LBL: Form the white cross on the bottom (D) face.
        This assumes white edges may be in any position and orients them correctly.
        """
        # This is a simplified version. You should break this into multiple passes:
        # 1. Move white edges from middle/bottom to top layer.
        # 2. Align and insert them from top layer to bottom face.

        # For now, here's a hardcoded example to illustrate the mechanism.
        # Later we can write full logic to find and move all white edges.

        # Example: Rotate the front face until white is on U face, then F2 to bring it down.
        for _ in range(4):  # do this for 4 sides: F, R, B, L
            top_color = self.cube.get_face('F')[0][1]  # top edge of F face
            if top_color == 'W':  # if it's white
                self.perform_move('F2')
            else:
                self.perform_move('U')
        
        # TODO: Add real logic to detect and position all white edges from all locations


    def solve_white_corners(self):
        # TODO: Implement white corners
        pass

    def solve_second_layer(self):
        # TODO: Solve the second (middle) layer
        pass

    def solve_yellow_cross(self):
        # TODO: Form the yellow cross on top
        pass

    def solve_yellow_edges(self):
        # TODO: Position the yellow edges
        pass

    def position_yellow_corners(self):
        # TODO: Position the yellow corners
        pass

    def orient_yellow_corners(self):
        # TODO: Rotate yellow corners to finish
        pass
    