# main.py

from solver.cube import RubiksCube

if __name__ == "__main__":
    cube = RubiksCube()

    print("Before U rotation:")
    cube.display()