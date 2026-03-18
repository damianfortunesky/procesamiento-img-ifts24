"""
TP01 - Punto de entrada

Este archivo inicializa un sketch básico con py5 para validar el entorno
y servir como base para futuros ejercicios de procesamiento de imágenes.
"""

import py5

WIDTH = 600
HEIGHT = 400


def setup():
    py5.size(WIDTH, HEIGHT)
    py5.background(240)

    py5.fill(0)
    py5.text_size(16)
    py5.text("TP01 - py5 funcionando correctamente", 50, 200)


def draw():
    pass


# IMPORTANTE: esto debe estar en el nivel global
py5.run_sketch()