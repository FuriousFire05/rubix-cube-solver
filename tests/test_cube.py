# tests/test_cube.py

import sys
import os

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.cube import RubiksCube
from utils.faces import Face


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


def test_get_face_invalid_face():
    cube = RubiksCube()

    with pytest.raises(KeyError):
        cube.get_face(
            "InvalidFace"
        )  # because _get_face expects a Face Enum, not string


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
