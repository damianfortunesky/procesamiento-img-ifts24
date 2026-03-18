"""TP01 - Pizarra interactiva con paleta de colores usando py5."""

import py5

WIDTH = 900
HEIGHT = 600
PALETTE_HEIGHT = 90
BRUSH_SIZE = 8

PALETTE_COLORS = [
    (0, 0, 0),
    (220, 30, 30),
    (30, 170, 60),
    (30, 90, 220),
    (255, 170, 0),
]

selected_color = PALETTE_COLORS[0]
color_buttons = []


def reset_canvas() -> None:
    """Limpia el área de dibujo y vuelve a dibujar la paleta."""
    py5.background(245)
    draw_palette()


def draw_palette() -> None:
    """Dibuja la franja de paleta y sus botones de color."""
    py5.no_stroke()
    py5.fill(225)
    py5.rect(0, 0, WIDTH, PALETTE_HEIGHT)

    for x, y, size, color in color_buttons:
        py5.fill(*color)
        py5.stroke(50)
        py5.stroke_weight(1)
        py5.rect(x, y, size, size, 6)

        if color == selected_color:
            py5.no_fill()
            py5.stroke(255)
            py5.stroke_weight(3)
            py5.rect(x - 3, y - 3, size + 6, size + 6, 8)


def setup() -> None:
    """Inicializa la ventana, la paleta y el lienzo."""
    py5.size(WIDTH, HEIGHT)

    button_size = 42
    margin = 16
    start_x = 20
    y = (PALETTE_HEIGHT - button_size) // 2

    for index, color in enumerate(PALETTE_COLORS):
        x = start_x + index * (button_size + margin)
        color_buttons.append((x, y, button_size, color))

    reset_canvas()


def draw() -> None:
    """Renderiza dibujo libre cuando el mouse está presionado."""
    if py5.is_mouse_pressed and py5.mouse_y >= PALETTE_HEIGHT:
        py5.stroke(*selected_color)
        py5.stroke_weight(BRUSH_SIZE)
        py5.line(py5.pmouse_x, py5.pmouse_y, py5.mouse_x, py5.mouse_y)


def mouse_pressed() -> None:
    """Selecciona color activo cuando se hace click sobre la paleta."""
    global selected_color

    if py5.mouse_y > PALETTE_HEIGHT:
        return

    for x, y, size, color in color_buttons:
        if x <= py5.mouse_x <= x + size and y <= py5.mouse_y <= y + size:
            selected_color = color
            draw_palette()
            break


def key_pressed() -> None:
    """Limpia el lienzo con la tecla C."""
    if py5.key and py5.key.lower() == "c":
        reset_canvas()


py5.run_sketch()
