# visualizer/UI.py

import pygame
from utils.faces import Face
from core.cube import RubiksCube
from core.moves import apply_move
from core.scramble import Scrambler
from visualizer.ui_state import UIState
from solver.kociemba import Kociemba_Solver
from visualizer.buttons import Button, RotatingColorButton
from solver.validation import validate_input_state


# Initialize pygame
pygame.init()

# Get the screen resolution
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Set up display
WIDTH, HEIGHT = screen_width, screen_height
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rubik's Cube Display")

# Place for Displaying History
history_rect = pygame.Rect(WIDTH - 250, 50, 200, HEIGHT - 100)

# Place for Displaying Solution
solution_rect = pygame.Rect(
    history_rect.x - history_rect.width - 20,
    history_rect.y,
    history_rect.width,
    history_rect.height,
)

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


# Displays Solution Steps (just like move history)
def draw_solution(screen, solution_moves, font, rect, offset):
    pygame.draw.rect(screen, (30, 30, 30), rect)  # dark background
    pygame.draw.rect(screen, (255, 255, 255), rect, 2)  # White border

    padding = 10
    y_offset = rect.top + padding + offset
    line_height = font.get_height() + 5

    for i, move in enumerate(solution_moves):
        move_text = font.render(f"{i+1}. {move}", True, (255, 255, 255))
        text_rect = move_text.get_rect(topleft=(rect.left + padding, y_offset))
        if rect.top <= text_rect.top <= rect.bottom:
            screen.blit(move_text, text_rect)
        y_offset += line_height


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


# Displays Moves as they are used
def draw_move_history(screen, history, font, rect, offset):
    pygame.draw.rect(screen, (30, 30, 30), rect)  # dark background
    pygame.draw.rect(screen, (255, 255, 255), rect, 2)  # White border

    padding = 10
    y_offset = rect.top + padding + offset
    line_height = font.get_height() + 5

    for i, move in enumerate(history[-len(history) :]):
        move_text = font.render(f"{i+1}. {move}", True, (255, 255, 255))
        text_rect = move_text.get_rect(topleft=(rect.left + padding, y_offset))
        if rect.top <= text_rect.top <= rect.bottom:
            screen.blit(move_text, text_rect)
        y_offset += line_height


# Brief Flash for Resetting State
def flash_screen(duration=150):
    """Brief white flash to indicate reset."""
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(180)  # Transparency level
    overlay.fill((255, 255, 255))  # White flash

    screen.blit(overlay, (0, 0))
    pygame.display.update()
    pygame.time.delay(duration)  # milliseconds


# Define button sizes and positions
button_width = 100
button_height = 50
button_spacing = 20
button_area_height = HEIGHT // 2  # Buttons will occupy the bottom half of the screen

# Define Button for Printing Solution
solve_button = Button(
    50,  # x position
    button_area_height + 350,  # y position
    button_width,
    button_height,
    (0, 255, 0),  # Green button
    "SOLVE",
)

input_button = Button(
    200,  # adjust position if needed
    button_area_height + 350,
    button_width,
    button_height,
    (0, 200, 200),  # cyan-ish color
    "INPUT",
)

# Define Button for Scrambling
scramble_button = RotatingColorButton(
    50 + (button_width + button_spacing) * 10,
    button_area_height + 50,
    button_width,
    button_height,
    colors=[RED, ORANGE, BLUE, YELLOW],
    text="SCRAMBLE",
    rotation_speed=100,
)

# Define Reset Button
reset_button = RotatingColorButton(
    200 + (button_width + button_spacing) * 10,
    button_area_height + 50,
    button_width,
    button_height,
    colors=[(0, 255, 0)],  # Green color for the reset button
    text="RESET",
)

clear_button = Button(
    history_rect.x, history_rect.bottom, history_rect.width, 30, (200, 0, 0), "CLEAR"
)

validate_button = Button(
    history_rect.x - 120,
    history_rect.bottom,
    100,
    30,
    (0, 200, 0),
    "VALIDATE",
)

cancel_button = Button(
    history_rect.x - 240,
    history_rect.bottom,
    100,
    30,
    (200, 200, 0),
    "CANCEL",
)

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

# Second row: Twice functions
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

# Third row: Counter-Clockwise (PRIME) functions
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

color_buttons = [
    Button(50 + i * (button_width + 10), button_area_height + 420, button_width, button_height, color, label)
    for i, (label, color) in enumerate([
        ("W", WHITE),
        ("Y", YELLOW),
        ("R", RED),
        ("O", ORANGE),
        ("B", BLUE),
        ("G", GREEN),
    ])
]

move_buttons = (
    buttons_row_1
    + buttons_row_2
    + buttons_row_3
    + [scramble_button, reset_button, solve_button, input_button]
)

input_mode_buttons = (
    color_buttons
    + [clear_button, validate_button, cancel_button]
)

def color_map(c):
    return {
        "W": WHITE,
        "Y": YELLOW,
        "R": RED,
        "O": ORANGE,
        "B": BLUE,
        "G": GREEN,
    }[c]

def get_clicked_sticker(pos):
    x_click, y_click = pos
    sticker_size = FACE_SIZE // 3

    for face, (x, y) in FACE_POSITIONS.items():
        for row in range(3):
            for col in range(3):
                rect = pygame.Rect(
                    x + col * sticker_size,
                    y + row * sticker_size,
                    sticker_size,
                    sticker_size,
                )
                if rect.collidepoint(x_click, y_click):
                    return face, row, col

    return None

# Main display function (UI logic)
def display_cube(cube: RubiksCube, scrambler: Scrambler):
    """Display the Rubik's Cube using Pygame."""
    running = True

    font = pygame.font.SysFont(None, 24)

    state = UIState()
    state.mode = "move"

    state.solution_moves = []
    state.solution_offset = 0
    state.history_offset = 0

    SCROLL_STEP = 20  # pixels to scroll per wheel event

    while running:
        screen.fill((100, 100, 100))  # grey background

        # Draw Move History window
        draw_move_history(screen, cube.move_history, font, history_rect, state.history_offset)
        draw_solution(screen, state.solution_moves, font, solution_rect, state.solution_offset)

        # Draw the Rubik's Cube faces
        for face, (x, y) in FACE_POSITIONS.items():
            if state.mode == "input":
                face_colors = [
                    [color_map(state.input_state.get_color(face.name, r, c)) for c in range(3)]
                    for r in range(3)
                ]
                draw_face(x, y, face_colors)
            else:
                draw_face(x, y, cube.get_face(face))

        # Draw buttons
        active_buttons = move_buttons if state.mode == "move" else input_mode_buttons

        for button in active_buttons:
            button.draw(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_clicked = False
                # Scroll wheel up
                if event.button == 4:
                    state.history_offset += SCROLL_STEP
                    state.solution_offset += SCROLL_STEP

                # Scroll wheel down
                elif event.button == 5:
                    state.history_offset -= SCROLL_STEP
                    state.solution_offset -= SCROLL_STEP

                # Clamp scrolling to limits
                state.history_offset = min(state.history_offset, 0)
                state.solution_offset = min(state.solution_offset, 0)

                active_buttons = move_buttons if state.mode == "move" else input_mode_buttons

                for button in active_buttons:
                    if button.is_clicked(event.pos):
                        button_clicked = True
                        if button.text == "CLEAR":
                            cube.move_history.clear()
                            state.solution_moves.clear()
                            state.history_offset = 0
                            state.solution_offset = 0
                            state.status_message = "History Cleared"
                        elif button.text == "SCRAMBLE":
                            scramble = scrambler.generate_scramble()
                            scrambler.apply_scramble(cube, scramble)
                            state.status_message = "Cube Scrambled"
                        elif button.text == "RESET":
                            flash_screen()
                            cube = RubiksCube()
                            state.status_message = "Cube Reset"
                        elif button.text == "SOLVE":
                            solver = Kociemba_Solver(cube)
                            state.solution_moves = solver.get_solution()
                            state.solution_offset = 0
                            state.status_message = "Solution Generated"
                        elif button.text == "INPUT":
                            if state.mode == "move":
                                state.mode = "input"
                                state.status_message = "Input Mode Active"
                            else:
                                state.mode = "move"
                                state.status_message = "Move Mode Active"
                        elif button.text in ["W", "Y", "R", "O", "B", "G"]:
                            state.selected_color = button.text
                            state.status_message = f"Selected Color: {button.text}"
                        elif button.text == "VALIDATE":
                            is_valid, message = validate_input_state(state.input_state)

                            if is_valid:
                                state.status_message = "Cube Validated Successfully"
                            else:
                                state.status_message = message
                        elif button.text == "CANCEL":
                            state.mode = "move"
                            state.status_message = "Input Cancelled"
                        else:
                            move = button.text
                            apply_move(cube, move)
                    
                    # Handle sticker clicks in input mode
                    if state.mode == "input" and state.selected_color:
                        result = get_clicked_sticker(event.pos)
                        if result:
                            face, row, col = result
                            state.input_state.set_color(face.name, row, col, state.selected_color)
                    
                    # Handle sticker clicks in input mode (only if no button was clicked)
                    if not button_clicked and state.mode == "input" and state.selected_color:
                        result = get_clicked_sticker(event.pos)
                        if result:
                            face, row, col = result
                            state.input_state.set_color(face.name, row, col, state.selected_color)

        # --- MODE DISPLAY ---
        mode_text = font.render(f"MODE: {state.mode.upper()}", True, (255, 255, 255))
        screen.blit(mode_text, (50, 10))

        # --- STATUS DISPLAY ---
        status_text = font.render(f"STATUS: {state.status_message}", True, (255, 255, 255))
        screen.blit(status_text, (50, 35))

        # Update the display after each move
        pygame.display.update()
    pygame.quit()
