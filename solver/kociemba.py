# solver/kociemba.py

"""
kociemba.py

Solver wrapper for the Kociemba algorithm.

This module provides a thin abstraction over the external kociemba solver
and is responsible for:
- accepting a RubiksCube instance
- converting the cube into solver string format
- returning the generated solution as a move list

This keeps solving logic separate from the UI and cube engine.
"""

import kociemba
from core.cube import RubiksCube


class Kociemba_Solver:
    def __init__(self, cube: RubiksCube):
        self.cube_string = cube.toString()

    def get_solution(self):
        return kociemba.solve(self.cube_string).split()
