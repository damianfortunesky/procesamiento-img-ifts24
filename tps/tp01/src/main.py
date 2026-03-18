"""Pizarra interactiva simple para TP01 usando py5."""

import py5

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
PALETTE_HEIGHT = 70
COLOR_SWATCH_SIZE = 42
COLOR_SWATCH_GAP = 14
PALETTE_MARGIN_X = 16
PALETTE_MARGIN_Y = 14

PALETTE_COLORS = [
    (0, 0, 0),      # black
    (220, 20, 60),  # red
    (46, 139, 87),  # green
    (30, 144, 255), # blue
    (255, 165, 0),  # orange
]

selected_color_index = 0


def setup() -> None:
    py5.size(WINDOW_WIDTH, WINDOW_HEIGHT)
    py5.background(255)
    py5.stroke_weight(4)
    py5.smooth()


def draw() -> None:
    draw_palette()


def draw_palette() -> None:
    py5.no_stroke()
    py5.fill(245)
    py5.rect(0, 0, py5.width, PALETTE_HEIGHT)

    for index, color in enumerate(PALETTE_COLORS):
        x = PALETTE_MARGIN_X + index * (COLOR_SWATCH_SIZE + COLOR_SWATCH_GAP)
        y = PALETTE_MARGIN_Y

        py5.fill(*color)
        py5.rect(x, y, COLOR_SWATCH_SIZE, COLOR_SWATCH_SIZE, 8)

        if index == selected_color_index:
            py5.no_fill()
            py5.stroke(30)
            py5.stroke_weight(3)
            py5.rect(x - 3, y - 3, COLOR_SWATCH_SIZE + 6, COLOR_SWATCH_SIZE + 6, 10)
            py5.stroke_weight(4)


def mouse_pressed() -> None:
    if py5.mouse_y <= PALETTE_HEIGHT:
        update_selected_color(py5.mouse_x, py5.mouse_y)


def mouse_dragged() -> None:
    if py5.mouse_y <= PALETTE_HEIGHT or py5.pmouse_y <= PALETTE_HEIGHT:
        return

    py5.stroke(*PALETTE_COLORS[selected_color_index])
    py5.line(py5.pmouse_x, py5.pmouse_y, py5.mouse_x, py5.mouse_y)


def key_pressed() -> None:
    if str(py5.key).lower() == "c":
        py5.background(255)


def update_selected_color(mouse_x: int, mouse_y: int) -> None:
    global selected_color_index

    for index in range(len(PALETTE_COLORS)):
        x = PALETTE_MARGIN_X + index * (COLOR_SWATCH_SIZE + COLOR_SWATCH_GAP)
        y = PALETTE_MARGIN_Y

        inside_x = x <= mouse_x <= x + COLOR_SWATCH_SIZE
        inside_y = y <= mouse_y <= y + COLOR_SWATCH_SIZE

        if inside_x and inside_y:
            selected_color_index = index
            break


if __name__ == "__main__":
    py5.run_sketch()
