# tests/test_pieces.py

import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.pieces import Piece, Center, Edge, Corner
from utils.colors import Color
from utils.faces import Face


def test_piece_initialization():
    # Initial colors - YELLOW on U face
    initial_colors = {Color.YELLOW: Face.U}
    position = (0, 1, 0)
    name = "test_piece"
    piece = Piece(initial_colors, name, position)

    assert piece.get_position() == position
    assert piece.get_faces() == initial_colors
    assert piece.get_name() == name

    # Test setters
    new_position = (1, 1, 1)
    piece.set_position(new_position)
    assert piece.get_position() == new_position

    # Test set_faces - should only update face assignments, not colors
    # We're keeping YELLOW but changing its face assignment to D
    new_face_assignments = {Color.YELLOW: Face.D}
    piece.set_faces(new_face_assignments)

    # Should have same colors but updated faces
    assert piece.get_faces() == new_face_assignments
    assert set(piece.get_faces().keys()) == {Color.YELLOW}  # Color didn't change

    # Trying to set faces for a color not on the piece should do nothing
    invalid_face_assignments = {Color.WHITE: Face.D}
    piece.set_faces(invalid_face_assignments)
    assert piece.get_faces() == new_face_assignments  # Should remain unchanged

    new_name = "updated_piece"
    piece.set_name(new_name)
    assert piece.get_name() == new_name

    # Test __repr__
    assert (
        repr(piece)
        == f"Piece(Colors: {new_face_assignments}, Position: {new_position})"
    )


def test_center_initialization():
    colors = {Color.YELLOW: Face.U}
    position = (0, 1, 0)
    name = "center_piece"
    center = Center(colors, name, position)

    assert center.get_position() == position
    assert center.get_faces() == colors
    assert center.get_name() == name

    # Test invalid center initialization
    with pytest.raises(
        ValueError, match="Center piece must have exactly 1 color and 1 face."
    ):
        Center({Color.YELLOW: Face.U, Color.WHITE: Face.D}, "invalid", (0, 0, 0))


def test_edge_initialization():
    colors = {Color.BLUE: Face.F, Color.RED: Face.R}
    position = (1, 0, 1)
    name = "edge_piece"
    edge = Edge(colors, name, position)

    assert edge.get_position() == position
    assert edge.get_faces() == colors
    assert edge.get_name() == name

    # Test invalid edge initialization
    with pytest.raises(
        ValueError, match="Edge piece must have exactly 2 colors and 2 faces."
    ):
        Edge({Color.YELLOW: Face.U}, "invalid", (0, 0, 0))


def test_corner_initialization():
    colors = {Color.YELLOW: Face.U, Color.BLUE: Face.F, Color.RED: Face.R}
    position = (1, 1, 1)
    name = "corner_piece"
    corner = Corner(colors, name, position)

    assert corner.get_position() == position
    assert corner.get_faces() == colors
    assert corner.get_name() == name

    # Test invalid corner initialization
    with pytest.raises(
        ValueError, match="Corner piece must have exactly 3 colors and 3 faces."
    ):
        Corner({Color.YELLOW: Face.U, Color.BLUE: Face.F}, "invalid", (0, 0, 0))
