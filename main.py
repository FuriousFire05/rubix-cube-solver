# main.py

"""Entry point to run the Rubik's Cube solver."""

from core.cube import RubiksCube
from core.scramble import Scrambler
from visualizer.UI import display_cube

if __name__ == "__main__":
    scrambler = Scrambler()
    cube = RubiksCube()

    scramble = scrambler.generate_scramble()
    scrambler.apply_scramble(cube, scramble)

    print("All moves made on cube so far:", cube.move_history)
    display_cube(cube)
