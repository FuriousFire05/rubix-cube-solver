class RubiksCube:
    def __init__(self):
        # Each face is a 3x3 grid with a single color
        # U = Up, D = Down, F = Front, B = Back, L = Left, R = Right
        self.faces = {
            'U': [['Y'] * 3 for _ in range(3)],  # Yellow   (Up)
            'D': [['W'] * 3 for _ in range(3)],  # White    (Down)
            'F': [['B'] * 3 for _ in range(3)],  # Blue     (Front)
            'B': [['G'] * 3 for _ in range(3)],  # Green    (Back)
            'L': [['O'] * 3 for _ in range(3)],  # Orange   (Left)
            'R': [['R'] * 3 for _ in range(3)],  # Red      (Right)
        }

    def display(self):
        for face, grid in self.faces.items():
            print(f"{face} face:")
            for row in grid:
                print(" ".join(row))
            print()