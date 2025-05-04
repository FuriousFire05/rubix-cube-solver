# solver/kociemba.py

import kociemba
from core.cube import RubiksCube


class Kociemba_Solver:
    def __init__(self, cube: RubiksCube):
        self.cube_string = cube.toString()

    def get_solution(self):
        return kociemba.solve(self.cube_string).split()
