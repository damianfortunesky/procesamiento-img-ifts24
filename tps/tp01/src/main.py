"""TP01 - Pizarra interactiva con paleta de colores usando py5."""

from dataclasses import dataclass

import py5

WIDTH = 900
HEIGHT = 600
PALETTE_HEIGHT = 90
DEFAULT_BRUSH_SIZE = 8
MIN_BRUSH_SIZE = 1
MAX_BRUSH_SIZE = 50
BACKGROUND_COLOR = (245, 245, 245)
TOOL_PENCIL = "Pencil"
TOOL_ERASER = "Eraser"

PALETTE_COLORS = [
    (0, 0, 0),
    (220, 30, 30),
    (30, 170, 60),
    (30, 90, 220),
    (255, 170, 0),
]


@dataclass
class BoardState:
    """Estado centralizado de la pizarra."""

    selected_color: tuple[int, int, int] = PALETTE_COLORS[0]
    active_tool: str = TOOL_PENCIL
    brush_size: int = DEFAULT_BRUSH_SIZE


state = BoardState()
color_buttons = []
tool_buttons = []


def draw_hud() -> None:
    """Dibuja información de herramienta, color y grosor activos."""
    hud_x = 320
    hud_y = 14
    hud_width = 560
    hud_height = 62

    py5.no_stroke()
    py5.fill(255, 255, 255, 220)
    py5.rect(hud_x, hud_y, hud_width, hud_height, 10)

    py5.fill(35)
    py5.text_size(15)
    py5.text(f"Herramienta: {state.active_tool}", hud_x + 12, hud_y + 24)
    py5.text(f"Grosor: {state.brush_size}", hud_x + 12, hud_y + 46)

    # Indicador de color actual como un círculo
    py5.text(f"Color:", hud_x + 220, hud_y + 35)
    py5.fill(*state.selected_color)
    py5.stroke(50)
    py5.stroke_weight(1)
    py5.circle(hud_x + 320, hud_y + 34, 18)


def draw_tool_buttons() -> None:
    """Dibuja botones de herramienta y resalta la herramienta activa."""
    for x, y, width, height, tool_name, label in tool_buttons:
        is_active = state.active_tool == tool_name

        py5.stroke(255 if is_active else 65)
        py5.stroke_weight(2 if is_active else 1)
        py5.fill(95, 95, 115) if is_active else py5.fill(225, 225, 238)
        py5.rect(x, y, width, height, 9)

        py5.fill(245 if is_active else 45)
        py5.text_size(13)
        py5.text_align(py5.CENTER, py5.CENTER)
        py5.text(label, x + width / 2, y + height / 2)

    py5.text_align(py5.LEFT, py5.BASELINE)


def reset_canvas() -> None:
    """Limpia el área de dibujo y vuelve a dibujar la paleta."""
    py5.background(*BACKGROUND_COLOR)
    draw_palette()
    draw_hud()


def draw_palette() -> None:
    """Dibuja la franja de paleta y sus botones de color."""
    py5.no_stroke()
    py5.fill(220, 220, 240)
    py5.rect(0, 0, WIDTH, PALETTE_HEIGHT)

    # Separador entre paleta y lienzo
    py5.stroke(180)
    py5.stroke_weight(2)
    py5.line(0, PALETTE_HEIGHT, WIDTH, PALETTE_HEIGHT)

    for cx, cy, radius, color in color_buttons:
        py5.fill(*color)
        py5.stroke(50)
        py5.stroke_weight(1)
        py5.circle(cx, cy, radius * 2)

        if color == state.selected_color:
            py5.no_fill()
            py5.stroke(255)
            py5.stroke_weight(3)
            py5.circle(cx, cy, radius * 2 + 8)

    draw_tool_buttons()


def setup() -> None:
    """Inicializa la ventana, la paleta y el lienzo."""
    py5.size(WIDTH, HEIGHT)

    button_radius = 20
    margin = 24
    start_x = 40
    y = PALETTE_HEIGHT // 2

    for index, color in enumerate(PALETTE_COLORS):
        cx = start_x + index * (button_radius * 2 + margin)
        color_buttons.append((cx, y, button_radius, color))

    tool_buttons.extend(
        [
            (535, 18, 110, 34, TOOL_PENCIL, "Lápiz (P)"),
            (655, 18, 110, 34, TOOL_ERASER, "Goma (E)"),
        ]
    )

    reset_canvas()


def draw() -> None:
    """Renderiza dibujo libre cuando el mouse está presionado."""
    if py5.is_mouse_pressed and py5.mouse_y >= PALETTE_HEIGHT:
        stroke_color = (
            state.selected_color
            if state.active_tool == TOOL_PENCIL
            else BACKGROUND_COLOR
        )
        py5.stroke(*stroke_color)
        py5.stroke_weight(state.brush_size)
        py5.line(py5.pmouse_x, py5.pmouse_y, py5.mouse_x, py5.mouse_y)


def mouse_pressed() -> None:
    """Selecciona color activo cuando se hace click sobre la paleta."""
    if py5.mouse_y > PALETTE_HEIGHT:
        return

    for x, y, width, height, tool_name, _ in tool_buttons:
        if x <= py5.mouse_x <= x + width and y <= py5.mouse_y <= y + height:
            state.active_tool = tool_name
            draw_palette()
            draw_hud()
            return

    for cx, cy, radius, color in color_buttons:
        if py5.dist(py5.mouse_x, py5.mouse_y, cx, cy) <= radius:
            state.selected_color = color
            draw_palette()
            draw_hud()
            break


def key_pressed() -> None:
    """Gestiona limpieza, cambio de herramientas y grosor de trazo."""
    if py5.key and py5.key.lower() == "p":
        state.active_tool = TOOL_PENCIL
        draw_palette()
        draw_hud()
        return

    if py5.key and py5.key.lower() == "e":
        state.active_tool = TOOL_ERASER
        draw_palette()
        draw_hud()
        return

    if py5.key and py5.key == "+":
        state.brush_size = min(MAX_BRUSH_SIZE, state.brush_size + 1)
        draw_palette()
        draw_hud()
        return

    if py5.key and py5.key == "-":
        state.brush_size = max(MIN_BRUSH_SIZE, state.brush_size - 1)
        draw_palette()
        draw_hud()
        return

    if py5.key and py5.key.lower() == "c":
        reset_canvas()


py5.run_sketch()
