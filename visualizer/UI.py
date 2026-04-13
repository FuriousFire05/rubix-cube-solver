# visualizer/UI.py

import pygame
from copy import deepcopy

from core.cube import RubiksCube
from core.moves import apply_move
from core.scramble import Scrambler
from solver.kociemba import Kociemba_Solver
from utils.colors import Color
from utils.faces import Face
from visualizer.buttons import Button, RotatingColorButton
from visualizer.ui_state import UIState


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
history_rect = pygame.Rect(WIDTH - 260, 40, 220, HEIGHT - 80)

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
GREY = (100, 100, 100)

CENTER_X = WIDTH // 2 - 150
CENTER_Y = HEIGHT // 2 - 150

FACE_POSITIONS = {
    Face.U: (CENTER_X, CENTER_Y - 180),
    Face.L: (CENTER_X - 180, CENTER_Y),
    Face.F: (CENTER_X, CENTER_Y),
    Face.R: (CENTER_X + 180, CENTER_Y),
    Face.B: (CENTER_X + 360, CENTER_Y),
    Face.D: (CENTER_X, CENTER_Y + 180),
}

FACE_SIZE = 150

COLOR_CODE_TO_ENUM = {
    "W": Color.WHITE,
    "Y": Color.YELLOW,
    "B": Color.BLUE,
    "G": Color.GREEN,
    "R": Color.RED,
    "O": Color.ORANGE,
}


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
    sticker_size = FACE_SIZE // 3

    for i in range(3):
        for j in range(3):
            pygame.draw.rect(
                screen,
                colors[i][j],
                (
                    x + j * sticker_size,
                    y + i * sticker_size,
                    sticker_size,
                    sticker_size,
                ),
                0,
            )
            pygame.draw.rect(
                screen,
                BLACK,
                (
                    x + j * sticker_size,
                    y + i * sticker_size,
                    sticker_size,
                    sticker_size,
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
    overlay.set_alpha(180)
    overlay.fill(WHITE)

    screen.blit(overlay, (0, 0))
    pygame.display.update()
    pygame.time.delay(duration)


# -------------------------
# Button setup
# -------------------------

# --- LAYOUT CONFIG ---
LEFT_PANEL_X = 40
BASE_Y = HEIGHT // 2 - 120

ROW_GAP = 80
BTN_W = 90
BTN_H = 50
BTN_GAP = 15

# Derived row positions
MOVES_Y_1 = BASE_Y
MOVES_Y_2 = BASE_Y + ROW_GAP
MOVES_Y_3 = BASE_Y + ROW_GAP * 2

ACTIONS_Y = MOVES_Y_3 + 80
INPUT_COLORS_Y = CENTER_Y + 260
INPUT_ACTIONS_Y = INPUT_COLORS_Y + 70

button_width = 100
button_height = 50
button_spacing = 20
button_area_height = HEIGHT // 2

solve_button = Button(
    LEFT_PANEL_X + 2 * (BTN_W + BTN_GAP),
    ACTIONS_Y,
    BTN_W,
    BTN_H,
    (0, 200, 0),
    "SOLVE",
)

input_button = Button(
    LEFT_PANEL_X + 3 * (BTN_W + BTN_GAP),
    ACTIONS_Y,
    BTN_W,
    BTN_H,
    (0, 200, 200),
    "INPUT",
)

scramble_button = RotatingColorButton(
    LEFT_PANEL_X,
    ACTIONS_Y,
    BTN_W,
    BTN_H,
    colors=[RED, ORANGE, BLUE, YELLOW],
    text="SCRAMBLE",
    rotation_speed=300,  # faster = more lively
)

reset_button = Button(
    LEFT_PANEL_X + (BTN_W + BTN_GAP),
    ACTIONS_Y,
    BTN_W,
    BTN_H,
    (210, 210, 210),
    "RESET",
)

validate_button = Button(
    LEFT_PANEL_X,
    INPUT_ACTIONS_Y,
    BTN_W,
    BTN_H,
    (0, 200, 0),
    "VALIDATE",
)

cancel_button = Button(
    LEFT_PANEL_X + (BTN_W + BTN_GAP),
    INPUT_ACTIONS_Y,
    BTN_W,
    BTN_H,
    (200, 200, 0),
    "CANCEL",
)

clear_button = Button(
    LEFT_PANEL_X + 2 * (BTN_W + BTN_GAP),
    INPUT_ACTIONS_Y,
    BTN_W,
    BTN_H,
    (200, 0, 0),
    "CLEAR",
)

history_clear_button = Button(
    history_rect.x,
    history_rect.bottom + 10,
    history_rect.width,
    30,
    (180, 0, 0),
    "CLEAR HISTORY",
)

solution_clear_button = Button(
    solution_rect.x,
    solution_rect.bottom + 10,
    solution_rect.width,
    30,
    (180, 0, 0),
    "CLEAR SOLUTION",
)

buttons_row_1 = [
    Button(
        LEFT_PANEL_X + i * (BTN_W + BTN_GAP),
        MOVES_Y_1,
        BTN_W,
        BTN_H,
        WHITE,
        move,
    )
    for i, move in enumerate(["U", "L", "F", "R", "B", "D"])
]

buttons_row_2 = [
    Button(
        LEFT_PANEL_X + i * (BTN_W + BTN_GAP),
        MOVES_Y_2,
        BTN_W,
        BTN_H,
        WHITE,
        move,
    )
    for i, move in enumerate(["U2", "L2", "F2", "R2", "B2", "D2"])
]

buttons_row_3 = [
    Button(
        LEFT_PANEL_X + i * (BTN_W + BTN_GAP),
        MOVES_Y_3,
        BTN_W,
        BTN_H,
        WHITE,
        move,
    )
    for i, move in enumerate(["U'", "L'", "F'", "R'", "B'", "D'"])
]

color_buttons = [
    Button(
        LEFT_PANEL_X + i * (BTN_W + BTN_GAP),
        INPUT_COLORS_Y,
        BTN_W,
        BTN_H,
        color,
        label,
    )
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
    + [history_clear_button, solution_clear_button]
)

input_mode_buttons = color_buttons + [clear_button, validate_button, cancel_button]


# -------------------------
# UI helpers
# -------------------------

def get_active_buttons(state):
    return move_buttons if state.mode == "move" else input_mode_buttons


def render_info_bar(font, state):
    mode_text = font.render(f"MODE: {state.mode.upper()}", True, WHITE)
    screen.blit(mode_text, (50, 10))

    status_text = font.render(f"STATUS: {state.status_message}", True, WHITE)
    screen.blit(status_text, (50, 35))

    selected = state.selected_color if state.selected_color else "-"
    selected_text = font.render(f"SELECTED: {selected}", True, WHITE)
    screen.blit(selected_text, (50, 60))


def render_move_mode(cube, state, font):
    draw_move_history(screen, cube.move_history, font, history_rect, state.history_offset)
    draw_solution(screen, state.solution_moves, font, solution_rect, state.solution_offset)

    for face, (x, y) in FACE_POSITIONS.items():
        draw_face(x, y, cube.get_face(face))


def render_input_mode(state, font):
    draw_move_history(screen, [], font, history_rect, state.history_offset)
    draw_solution(screen, state.solution_moves, font, solution_rect, state.solution_offset)

    if state.draft_cube is None:
        return

    for face, (x, y) in FACE_POSITIONS.items():
        draw_face(x, y, state.draft_cube.get_face(face))


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


def face_row_col_to_cube_position(face, row, col):
    """
    Convert a visible face cell (row, col) on the 2D net
    back to the corresponding cubie position (x, y, z).
    """
    if face == Face.U:
        return col, 2, row
    if face == Face.D:
        return col, 0, 2 - row
    if face == Face.F:
        return col, 2 - row, 2
    if face == Face.B:
        return 2 - col, 2 - row, 0
    if face == Face.R:
        return 2, 2 - row, 2 - col
    if face == Face.L:
        return 0, 2 - row, col
    raise ValueError(f"Unsupported face: {face}")


def set_piece_face_color(piece, visible_face, color_code):
    """
    Recolor the sticker on a piece that is currently facing `visible_face`.
    Returns (success, message).
    """
    if color_code not in COLOR_CODE_TO_ENUM:
        return False, f"Unknown color code: {color_code}"

    new_color = COLOR_CODE_TO_ENUM[color_code]
    face_map = piece.get_faces()

    current_color = None
    for color, piece_face in face_map.items():
        if piece_face == visible_face:
            current_color = color
            break

    if current_color is None:
        return False, "Selected sticker does not exist on this piece"

    if current_color == new_color:
        return True, "Sticker already has that color"

    # Piece model uses colors as dictionary keys, so duplicate colors on one piece
    # cannot be represented safely. Reject those edits.
    for color, piece_face in face_map.items():
        if color == new_color and piece_face != visible_face:
            return False, "That piece already uses this color"

    updated_faces = {}
    for color, piece_face in face_map.items():
        if piece_face == visible_face:
            updated_faces[new_color] = piece_face
        else:
            updated_faces[color] = piece_face

    piece.colors = updated_faces
    return True, "Sticker updated"


def set_draft_cube_sticker(draft_cube, face, row, col, color_code):
    """
    Apply a sticker edit directly onto the draft cube metadata.
    Centers are locked.
    """
    if draft_cube is None:
        return False, "No draft cube available"

    if row == 1 and col == 1:
        return False, "Center stickers cannot be edited"

    x, y, z = face_row_col_to_cube_position(face, row, col)
    piece = draft_cube.get_piece_at_position(x, y, z)

    if piece is None:
        return False, "No piece found at selected position"

    return set_piece_face_color(piece, face, color_code)


def validate_cube_counts(cube):
    """
    Quick color count validation using the rendered cube faces.
    """
    counts = {
        "WHITE": 0,
        "YELLOW": 0,
        "BLUE": 0,
        "GREEN": 0,
        "RED": 0,
        "ORANGE": 0,
    }

    for face in Face:
        face_grid = cube.get_face(face)
        for row in face_grid:
            for color_name in row:
                if color_name not in counts:
                    return False, f"Unexpected sticker color: {color_name}"
                counts[color_name] += 1

    for color_name, count in counts.items():
        if count != 9:
            return False, f"Invalid count for {color_name}: {count}"

    return True, "Color counts valid"


def validate_and_solve_draft_cube(draft_cube):
    """
    Validate the draft cube and return (is_valid, message, solution_moves).
    """
    counts_valid, counts_message = validate_cube_counts(draft_cube)
    if not counts_valid:
        return False, counts_message, []

    try:
        solution_moves = Kociemba_Solver(draft_cube).get_solution()
        return True, "Input validated successfully", solution_moves
    except Exception:
        return False, "Invalid cube configuration (unsolvable)", []


# -------------------------
# Main display function
# -------------------------

def display_cube(cube: RubiksCube, scrambler: Scrambler):
    """Display the Rubik's Cube using Pygame."""
    running = True
    font = pygame.font.SysFont(None, 24)

    state = UIState()
    state.mode = "move"
    state.solution_moves = []
    state.solution_offset = 0
    state.history_offset = 0
    state.selected_color = None
    state.draft_cube = None

    scroll_step = 20

    while running:
        screen.fill(GREY)

        if state.mode == "move":
            render_move_mode(cube, state, font)
        else:
            render_input_mode(state, font)

        active_buttons = get_active_buttons(state)
        for button in active_buttons:
            button.draw(screen)

        render_info_bar(font, state)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                button_clicked = False

                if event.button == 4:
                    state.history_offset += scroll_step
                    state.solution_offset += scroll_step

                elif event.button == 5:
                    state.history_offset -= scroll_step
                    state.solution_offset -= scroll_step

                state.history_offset = min(state.history_offset, 0)
                state.solution_offset = min(state.solution_offset, 0)

                active_buttons = get_active_buttons(state)

                for button in active_buttons:
                    if button.is_clicked(event.pos):
                        button_clicked = True

                        if button.text == "SCRAMBLE":
                            scramble = scrambler.generate_scramble()
                            scrambler.apply_scramble(cube, scramble)
                            state.status_message = "Cube scrambled"

                        elif button.text == "RESET":
                            flash_screen()
                            cube = RubiksCube()
                            state.solution_moves.clear()
                            state.solution_offset = 0
                            state.history_offset = 0
                            state.status_message = "Cube reset"

                        elif button.text == "SOLVE":
                            try:
                                state.solution_moves = Kociemba_Solver(cube).get_solution()
                                state.solution_offset = 0
                                state.status_message = "Solution generated"
                            except Exception:
                                state.status_message = "Error solving cube"

                        elif button.text == "INPUT":
                            state.mode = "input"
                            state.draft_cube = deepcopy(cube)
                            state.selected_color = None
                            state.solution_moves.clear()
                            state.solution_offset = 0
                            state.history_offset = 0
                            state.status_message = "Input mode active"

                        elif state.mode == "input" and button.text in ["W", "Y", "R", "O", "B", "G"]:
                            state.selected_color = button.text
                            state.status_message = f"Selected color: {button.text}"

                        elif button.text == "CLEAR":
                            state.draft_cube = deepcopy(cube)
                            state.selected_color = None
                            state.solution_moves.clear()
                            state.solution_offset = 0
                            state.history_offset = 0
                            state.status_message = "Input draft cleared"

                        elif button.text == "CLEAR HISTORY":
                            cube.move_history.clear()
                            state.history_offset = 0
                            state.status_message = "History cleared"

                        elif button.text == "CLEAR SOLUTION":
                            state.solution_moves.clear()
                            state.solution_offset = 0
                            state.status_message = "Solution cleared"

                        elif button.text == "VALIDATE":
                            if state.draft_cube is None:
                                state.status_message = "No draft cube to validate"
                            else:
                                is_valid, message, solution_moves = validate_and_solve_draft_cube(state.draft_cube)

                                if is_valid:
                                    cube = deepcopy(state.draft_cube)
                                    state.solution_moves = solution_moves
                                    state.solution_offset = 0
                                    state.mode = "move"
                                    state.draft_cube = None
                                    state.selected_color = None
                                    state.status_message = "Input validated and applied"
                                else:
                                    state.status_message = message

                        elif button.text == "CANCEL":
                            state.mode = "move"
                            state.draft_cube = None
                            state.selected_color = None
                            state.status_message = "Input cancelled"

                        else:
                            try:
                                apply_move(cube, button.text)
                                state.status_message = f"Move applied: {button.text}"
                            except Exception:
                                state.status_message = f"Invalid move: {button.text}"

                        break

                # Sticker editing happens only if no button was clicked
                if not button_clicked and state.mode == "input" and state.selected_color:
                    result = get_clicked_sticker(event.pos)
                    if result:
                        face, row, col = result
                        success, message = set_draft_cube_sticker(
                            state.draft_cube,
                            face,
                            row,
                            col,
                            state.selected_color,
                        )
                        state.status_message = message

        pygame.display.update()

    pygame.quit()