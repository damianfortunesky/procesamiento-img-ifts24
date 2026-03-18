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

```powershell: crear y lanzar entornno

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
py -m venv .venv
.venv\Scripts\Activate.ps1

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


# Entorno Virtual en Python (venv)

## Objetivo

El entorno virtual (`venv`) permite aislar las dependencias de un proyecto Python, evitando conflictos entre librerías y versiones utilizadas en distintos proyectos.

Cada proyecto mantiene sus propias dependencias, sin afectar al sistema global.

---

## ¿Por qué usar un entorno virtual?

- Evita conflictos entre versiones de librerías
- Permite reproducir el entorno fácilmente (`requirements.txt`)
- Mantiene el sistema limpio (no instala paquetes globales)
- Es estándar en proyectos profesionales

---

# 1. Crear entorno (una sola vez)
py -3.12 -m venv .venv

# 2. Activar entorno
.venv\Scripts\Activate.ps1

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Trabajar en el proyecto

# 5. Desactivar entorno
deactivate