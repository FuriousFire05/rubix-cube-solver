# tests/test_scramble.py

import sys
import os
from unittest.mock import MagicMock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.scramble import Scrambler


def test_scrambler_initialization():
    scrambler = Scrambler()
    assert scrambler.history == []
    assert len(scrambler.MOVES) == 18


def test_generate_scramble():
    scrambler = Scrambler()

    # Test default length
    scramble = scrambler.generate_scramble()
    assert len(scramble) == 20
    assert scramble in scrambler.history

    # Test no consecutive same face moves
    for i in range(len(scramble) - 1):
        assert scramble[i][0] != scramble[i + 1][0]

    # Test custom length
    short_scramble = scrambler.generate_scramble(5)
    assert len(short_scramble) == 5
    assert short_scramble in scrambler.history


def test_apply_scramble():
    scrambler = Scrambler()
    mock_cube = MagicMock()

    # Test all move types
    scramble = ["U", "U'", "U2", "F", "R'", "L2"]
    scrambler.apply_scramble(mock_cube, scramble)

    # Check that the correct methods were called
    mock_cube.U.assert_called_once()
    mock_cube.U_prime.assert_called_once()
    mock_cube.U2.assert_called_once()
    mock_cube.F.assert_called_once()
    mock_cube.R_prime.assert_called_once()
    mock_cube.L2.assert_called_once()


def test_scramble_history():
    scrambler = Scrambler()
    assert len(scrambler.history) == 0

    scramble1 = scrambler.generate_scramble(5)
    assert len(scrambler.history) == 1
    assert scramble1 in scrambler.history

    scramble2 = scrambler.generate_scramble(10)
    assert len(scrambler.history) == 2
    assert scramble1 in scrambler.history
    assert scramble2 in scrambler.history
