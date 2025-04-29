import random


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
            face = move[0]
            modifier = move[1:] if len(move) > 1 else ""

            if modifier == "":
                method = getattr(cube, face)  # e.g., U, D, F, B, R, L
            elif modifier == "'":
                method = getattr(cube, f"{face}_prime")  # e.g., U', D', F', B', R', L'
            elif modifier == "2":
                method = getattr(cube, f"{face}2")  # e.g., U2, D2, F2, B2, R2, L2

            method()  # Apply the selected move
