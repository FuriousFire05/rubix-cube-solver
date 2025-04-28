# main.py

"""Entry point to run the Rubik's Cube solver."""

from solver.cube import RubiksCube
from visualizer.UI import display_cube

if __name__ == "__main__":
    cube = RubiksCube()

    display_cube(cube)