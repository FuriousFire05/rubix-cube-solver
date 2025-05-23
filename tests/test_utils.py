# tests/test_utils.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.colors import Color
from utils.faces import Face


def test_color_enum_values():
    assert Color.YELLOW.value == "#FFFF00"
    assert Color.WHITE.value == "#FFFFFF"
    assert Color.BLUE.value == "#0000FF"
    assert Color.GREEN.value == "#00FF00"
    assert Color.RED.value == "#FF0000"
    assert Color.ORANGE.value == "#FFA500"


def test_face_enum():
    assert Face.U.name == "U"
    assert Face.D.name == "D"
    assert Face.F.name == "F"
    assert Face.B.name == "B"
    assert Face.R.name == "R"
    assert Face.L.name == "L"

    # Test face color associations
    assert Face.U.value == Color.YELLOW
    assert Face.D.value == Color.WHITE
    assert Face.F.value == Color.BLUE
    assert Face.B.value == Color.GREEN
    assert Face.R.value == Color.RED
    assert Face.L.value == Color.ORANGE


def test_color_string_representations():
    assert str(Color.YELLOW) == "Yellow"
    assert repr(Color.YELLOW) == "Color.YELLOW"


def test_face_string_representations():
    assert str(Face.U) == "U"
    assert repr(Face.U) == "Face.U"
