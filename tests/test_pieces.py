# tests/test_pieces.py

import sys
import os

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from solver.pieces import Piece, Center, Edge, Corner
from utils.colors import Color
from utils.faces import Face


def test_piece_initialization():
    colors = {Face.U: Color.YELLOW}
    position = (0, 1, 0)
    piece = Piece(colors, "", position)

    assert piece.get_position() == position
    assert piece.get_faces() == colors


def test_center_initialization():
    colors = {Face.U: Color.YELLOW}
    position = (0, 1, 0)
    center = Center(colors, "", position)

    assert center.get_position() == position
    assert center.get_faces() == colors


def test_edge_initialization():
    colors = {Face.F: Color.BLUE, Face.R: Color.RED}
    position = (1, 0, 1)
    edge = Edge(colors, "", position)

    assert edge.get_position() == position
    assert edge.get_faces() == colors


def test_corner_initialization():
    colors = {Face.U: Color.YELLOW, Face.F: Color.BLUE, Face.R: Color.RED}
    position = (1, 1, 1)
    corner = Corner(colors, "", position)

    assert corner.get_position() == position
    assert corner.get_faces() == colors
