# visualizer/visualizer.py

import pygame
from core.cube import RubiksCube
from utils.faces import Face
from visualizer.button import Button

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 1200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rubik's Cube Display")

# Define colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)

FACE_POSITIONS = {
    Face.U: (225, 50),
    Face.L: (50, 225),
    Face.F: (225, 225),
    Face.R: (400, 225),
    Face.B: (575, 225),
    Face.D: (225, 400),
}

FACE_SIZE = 150


# Function to draw a 3x3 face with different colors
def draw_face(x, y, colors):
    """Draw a 3x3 face of the Rubik's Cube."""
    STICKER_SIZE = FACE_SIZE // 3
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(
                screen,
                colors[i][j],
                (
                    x + j * STICKER_SIZE,
                    y + i * STICKER_SIZE,
                    STICKER_SIZE,
                    STICKER_SIZE,
                ),
                0,
            )
            pygame.draw.rect(
                screen,
                (0, 0, 0),  # black border
                (
                    x + j * STICKER_SIZE,
                    y + i * STICKER_SIZE,
                    STICKER_SIZE,
                    STICKER_SIZE,
                ),
                1,
            )


# Define button sizes and positions
button_width = 100
button_height = 50
button_spacing = 20
button_area_height = HEIGHT // 2  # Buttons will occupy the bottom half of the screen

# First row: Clockwise functions
buttons_row_1 = [
    Button(
        50 + (button_width + button_spacing) * i,
        button_area_height + 50,
        button_width,
        button_height,
        (255, 255, 255),
        move,
    )
    for i, move in enumerate(["U", "L", "F", "R", "B", "D"])
]

# Second row: Counter-clockwise (prime) functions
buttons_row_2 = [
    Button(
        50 + (button_width + button_spacing) * i,
        button_area_height + 150,
        button_width,
        button_height,
        (255, 255, 255),
        move,
    )
    for i, move in enumerate(["U2", "L2", "F2", "R2", "B2", "D2"])
]

buttons_row_3 = [
    Button(
        50 + (button_width + button_spacing) * i,
        button_area_height + 250,
        button_width,
        button_height,
        (255, 255, 255),
        move,
    )
    for i, move in enumerate(["U'", "L'", "F'", "R'", "B'", "D'"])
]

buttons = buttons_row_1 + buttons_row_2 + buttons_row_3


# Main display function (UI logic)
def display_cube(cube: RubiksCube):
    """Display the Rubik's Cube using Pygame."""
    running = True
    while running:
        screen.fill((100, 100, 100))  # grey background

        # Draw the Rubik's Cube faces
        for face, (x, y) in FACE_POSITIONS.items():
            draw_face(x, y, cube.get_face(face))

        # Draw buttons
        for button in buttons:
            button.draw(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.is_clicked(event.pos):
                        move = button.text
                        rotation_method = {
                            "U": cube.U,
                            "L": cube.L,
                            "F": cube.F,
                            "R": cube.R,
                            "B": cube.B,
                            "D": cube.D,
                            "U2": cube.U2,
                            "L2": cube.L2,
                            "F2": cube.F2,
                            "R2": cube.R2,
                            "B2": cube.B2,
                            "D2": cube.D2,
                            "U'": cube.U_prime,
                            "L'": cube.L_prime,
                            "F'": cube.F_prime,
                            "R'": cube.R_prime,
                            "B'": cube.B_prime,
                            "D'": cube.D_prime,
                        }
                        if move in rotation_method:
                            rotation_method[move]()

        # Update the display after each move
        pygame.display.update()
    pygame.quit()
