# main.py

"""Entry point to run the Rubik's Cube solver."""

from core.cube import RubiksCube
from core.scramble import Scrambler
from visualizer.UI import display_cube

if __name__ == "__main__":
    scrambler = Scrambler()
    cube = RubiksCube()

    display_cube(cube, scrambler)
