# main.py

"""
main.py

Application entry point for the Rubik's Cube simulator.

This script initializes the live cube and scrambler, then launches
the main Pygame UI loop.
"""

from core.cube import RubiksCube
from core.scramble import Scrambler
from visualizer.UI import display_cube


if __name__ == "__main__":
    cube = RubiksCube()
    scrambler = Scrambler()
    display_cube(cube, scrambler)
