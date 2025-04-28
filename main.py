# main.py

"""Entry point to run the Rubik's Cube solver."""

from solver.cube import RubiksCube


if __name__ == "__main__":
    cube = RubiksCube()
    cube.display()

    cube.L()

    cube.display()
