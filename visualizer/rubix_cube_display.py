# visualizer/rubix_cube_display.py

import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rubik's Cube Display")

# Define colors
WHITE = (255, 255, 255)  # D
YELLOW = (255, 255, 0)  # U
BLUE = (0, 0, 255)  # F
RED = (255, 0, 0)  # R
GREEN = (0, 255, 0)  # B
ORANGE = (255, 165, 0)  # L

# Face size
FACE_SIZE = 150


# Function to draw a 3x3 face with different colors
def draw_face(x, y, colors):
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


# Define cube faces (3x3 color grids)
U_face = [[YELLOW] * 3 for _ in range(3)]
L_face = [[ORANGE] * 3 for _ in range(3)]
F_face = [[BLUE] * 3 for _ in range(3)]
R_face = [[RED] * 3 for _ in range(3)]
B_face = [[GREEN] * 3 for _ in range(3)]
D_face = [[WHITE] * 3 for _ in range(3)]


# Main loop
def main():
    running = True
    while running:
        screen.fill((100, 100, 100))  # grey background

        # Draw faces with their individual color grids
        draw_face(225, 50, U_face)  # Up
        draw_face(50, 225, L_face)  # Left
        draw_face(225, 225, F_face)  # Front
        draw_face(400, 225, R_face)  # Right
        draw_face(575, 225, B_face)  # Back
        draw_face(225, 400, D_face)  # Down

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
    sys.exit()


# Run it
if __name__ == "__main__":
    main()
