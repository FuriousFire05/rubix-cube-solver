import random

class Scrambler:
    MOVES = [
        'U', "U'", 'U2',
        'D', "D'", 'D2',
        'F', "F'", 'F2',
        'B', "B'", 'B2',
        'R', "R'", 'R2',
        'L', "L'", 'L2'
    ]

    def __init__(self):
        self.history = []

    def generate_scramble(self, length=20):
        """
        Generate a random scramble and store it in history.
        Avoids repeating the same face consecutively.
        """
        scramble = []
        last_face = ''
        
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
            modifier = move[1:] if len(move) > 1 else ''

            method = None
            if modifier == '':
                method = getattr(cube, face)
            elif modifier == "'":
                method = getattr(cube, f'{face}_prime')
            elif modifier == '2':
                method = lambda: [getattr(cube, face)(), getattr(cube, face)()]

            method()
