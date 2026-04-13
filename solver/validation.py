# solver/validation.py

from solver.kociemba import Kociemba_Solver


def validate_input_state(input_state):
    """
    Validates the manually entered cube state.

    Returns:
        (bool, str): (is_valid, message)
    """

    # --- Step 1: Color Count Check ---
    counts = {}

    for face in input_state.get_all_faces().values():
        for row in face:
            for color in row:
                counts[color] = counts.get(color, 0) + 1

    required_colors = ["W", "Y", "R", "O", "B", "G"]

    for color in required_colors:
        if counts.get(color, 0) != 9:
            return False, f"Invalid count for {color}: {counts.get(color, 0)}"

    # --- Step 2: Convert to Kociemba string ---
    try:
        cube_string = convert_to_kociemba_string(input_state)
    except Exception:
        return False, "Error converting cube state"

    # --- Step 3: Solver Validation ---
    try:
        solver = Kociemba_Solver(cube_string)
        solver.get_solution()
        return True, "Cube is valid"
    except Exception:
        return False, "Invalid cube configuration (unsolvable)"


def convert_to_kociemba_string(input_state):
    """
    Converts InputState to Kociemba string format.

    Order required by Kociemba:
    U, R, F, D, L, B
    """

    face_order = ["U", "R", "F", "D", "L", "B"]

    color_to_face = {
        "Y": "U",
        "W": "D",
        "B": "F",
        "G": "B",
        "O": "L",
        "R": "R",
    }

    cube_string = ""

    for face in face_order:
        grid = input_state.get_all_faces()[face]
        for row in grid:
            for color in row:
                cube_string += color_to_face[color]

    return cube_string