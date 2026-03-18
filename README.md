# Procesamiento de Imágenes Digitales - Trabajos Prácticos

Repositorio base para desarrollar los trabajos prácticos (TPs) de la materia **Procesamiento de Imágenes Digitales** usando **Python 3** y **py5**.

## Objetivo del repositorio

- Centralizar el desarrollo de múltiples TPs en una estructura única.
- Mantener una organización simple y escalable.
- Facilitar el trabajo local desde Visual Studio Code.

## Requisitos

- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Java Runtime (requisito habitual de py5)

## Instalación del entorno

1. (Opcional) Crear y activar un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\\Scripts\\activate   # Windows (PowerShell)
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Estructura base

```text
.
├── README.md
├── requirements.txt
└── tps/
    └── tp01/
        ├── README.md
        ├── assets/
        │   ├── input/
        │   └── output/
        └── src/
            └── main.py
```

## Uso inicial

Ejecutar el TP de ejemplo:

```bash
python tps/tp01/src/main.py
```

Este TP inicial no implementa lógica de procesamiento todavía; solo deja el punto de entrada listo para comenzar.

## Convención para nuevos TPs

Para agregar un nuevo trabajo práctico, replicar la estructura de `tp01`:

- `assets/input/`: imágenes de entrada
- `assets/output/`: resultados generados
- `src/main.py`: punto de entrada del TP
- `README.md`: notas y consignas del TP
