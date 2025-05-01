# tests/test_cube.py

import sys
import os

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.cube import RubiksCube
from utils.faces import Face
from utils.colors import Color


def test_cube_initial_state():
    cube = RubiksCube()

    U = cube.get_face(Face.U)
    D = cube.get_face(Face.D)
    F = cube.get_face(Face.F)
    B = cube.get_face(Face.B)
    R = cube.get_face(Face.R)
    L = cube.get_face(Face.L)

    assert U[1][1] == "YELLOW", f"Expected Yellow at U center, got {U[1][1]}"
    assert D[1][1] == "WHITE", f"Expected White at D center, got {D[1][1]}"
    assert F[1][1] == "BLUE", f"Expected Blue at F center, got {F[1][1]}"
    assert B[1][1] == "GREEN", f"Expected Green at B center, got {B[1][1]}"
    assert R[1][1] == "RED", f"Expected Red at R center, got {R[1][1]}"
    assert L[1][1] == "ORANGE", f"Expected Orange at L center, got {L[1][1]}"


def test_initial_state_is_solved():
    cube = RubiksCube()
    assert cube.is_solved() is True


def test_get_face_returns_correct_center():
    cube = RubiksCube()
    for face in Face:
        face_grid = cube.get_face(face)
        center_color = face_grid[1][1]
        for row in face_grid:
            for color in row:
                assert color == center_color


def test_invalid_face_raises_key_error():
    cube = RubiksCube()
    with pytest.raises(KeyError):
        cube.get_face("INVALID")


def test_rotation_and_inverse_restores_state():
    cube = RubiksCube()
    original_state = str(cube.get_face(Face.F))
    cube.F()
    cube.F_prime()
    restored_state = str(cube.get_face(Face.F))
    assert restored_state == original_state
    assert cube.is_solved()


def test_double_rotations():
    cube = RubiksCube()
    original = str(cube.get_face(Face.U))
    cube.U2()
    cube.U2()
    assert str(cube.get_face(Face.U)) == original


def test_triple_rotations_is_inverse():
    cube1 = RubiksCube()
    cube2 = RubiksCube()
    cube1.L()
    cube1.L()
    cube1.L()
    cube2.L_prime()
    for face in Face:
        assert cube1.get_face(face) == cube2.get_face(face)


def test_move_history_tracking():
    cube = RubiksCube()
    cube.F()
    cube.R()
    cube.U2()
    assert cube.move_history == ["F", "R", "U2"]


def test_get_piece_at_position():
    cube = RubiksCube()
    piece = cube.get_piece_at_position(1, 2, 1)
    assert piece.get_name() == "U"


def test_find_piece_by_colors():
    cube = RubiksCube()
    piece = cube.find_piece_by_colors(Color.YELLOW, Color.BLUE, Color.RED)
    assert piece is not None
    assert set(piece.get_faces().keys()) == {Color.YELLOW, Color.BLUE, Color.RED}


def test_invalid_piece_in_fetch_components():
    cube = RubiksCube()
    with pytest.raises(ValueError):
        cube._fetch_components(["XXX"])


def test_rotate_components_invalid_face():
    cube = RubiksCube()
    comps = cube._fetch_components(["UF", "UR", "UB", "UL"])
    with pytest.raises(ValueError):
        cube._rotate_components(comps, "Z")


def test_print_matrix_runs():
    cube = RubiksCube()
    cube.print_matrix()  # Should not crash


def test_display_runs():
    cube = RubiksCube()
    cube.display()  # Should not crash


def test_apply_and_fetch_components_consistency():
    cube = RubiksCube()
    keys = ["DF", "DL", "DB", "DR"]
    comps = cube._fetch_components(keys)
    cube._apply_components(keys, comps)  # Should not raise
    assert cube._fetch_components(keys) == comps


def test_centers_created():
    cube = RubiksCube()

    centers = [
        piece for piece in cube.pieces.values() if piece.__class__.__name__ == "Center"
    ]
    assert len(centers) == 6, f"Expected 6 centers, got {len(centers)}"


def test_edges_created():
    cube = RubiksCube()

    edges = [
        piece for piece in cube.pieces.values() if piece.__class__.__name__ == "Edge"
    ]
    assert len(edges) == 12, f"Expected 12 edges, got {len(edges)}"


def test_corners_created():
    cube = RubiksCube()

    corners = [
        piece for piece in cube.pieces.values() if piece.__class__.__name__ == "Corner"
    ]
    assert len(corners) == 8, f"Expected 8 corners, got {len(corners)}"
