# core/scramble.py

"""
scramble.py

Scramble generation and application utilities.

This module is responsible for:
- generating random valid scramble sequences
- tracking scramble history
- applying scrambles to a RubiksCube instance

It uses standard cube notation and the shared move dispatch system.
"""

import random
from core.moves import apply_move

class Scrambler:
    # fmt: off
    MOVES = [
        'U', "U'", 'U2',
        'D', "D'", 'D2',
        'F', "F'", 'F2',
        'B', "B'", 'B2',
        'R', "R'", 'R2',
        'L', "L'", 'L2'
    ]
    # fmt: on

    def __init__(self):
        self.history = []

    def generate_scramble(self, length=20):
        """
        Generate a random scramble and store it in history.
        Avoids repeating the same face consecutively.
        """
        scramble = []
        last_face = ""

        for _ in range(length):
            move = random.choice(self.MOVES)
            while move[0] == last_face:
                move = random.choice(self.MOVES)
            scramble.append(move)
            last_face = move[0]

        self.history.append(scramble)
        return scramble

    def apply_scramble(self, cube, scramble):
        for move in scramble:
            apply_move(cube, move)