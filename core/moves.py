# core/moves.py

"""
moves.py

Move dispatch helper for the Rubik's Cube engine.

This module centralizes move execution by mapping standard cube notation
(e.g. U, R', F2) to the corresponding RubiksCube methods.

It is used to keep move logic consistent across:
- manual move button input
- scramble application
- future replay / animation systems
"""

from core.cube import RubiksCube

def apply_move(cube: RubiksCube, move: str) -> None:
    """
    Apply a move to the given Rubik's Cube instance.

    Args:
        cube (RubiksCube): The cube instance to modify.
        move (str): The move to apply (e.g., "U", "R'", "F2").

    Raises:
        TypeError: If cube or move is of incorrect type.
        ValueError: If move is not a valid cube move.
    """

    # --- Type validation ---
    if not isinstance(cube, RubiksCube):
        raise TypeError("cube must be an instance of RubiksCube")

    if not isinstance(move, str):
        raise TypeError("move must be a string")

    # --- Move mapping ---
    rotation_method = {
        "U": cube.U,
        "U2": cube.U2,
        "U'": cube.U_prime,

        "D": cube.D,
        "D2": cube.D2,
        "D'": cube.D_prime,

        "L": cube.L,
        "L2": cube.L2,
        "L'": cube.L_prime,

        "R": cube.R,
        "R2": cube.R2,
        "R'": cube.R_prime,

        "F": cube.F,
        "F2": cube.F2,
        "F'": cube.F_prime,

        "B": cube.B,
        "B2": cube.B2,
        "B'": cube.B_prime,
    }

    # --- Value validation ---
    if move not in rotation_method:
        raise ValueError(f"Invalid move: {move}")

    # --- Apply move ---
    rotation_method[move]()