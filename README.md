# Procesamiento de Imágenes Digitales - Trabajos Prácticos

Repositorio base para desarrollar trabajos prácticos de **Procesamiento de Imágenes Digitales** usando **Python 3.12** y **py5**.

## Objetivo

- Centralizar los TPs en una estructura única.
- Mantener una organización simple y escalable.
- Facilitar ejecución local en Visual Studio Code.

## Requisitos

- Python 3.12
- pip
- Java Runtime (requisito de py5)

## Instalación del entorno

### PowerShell (Windows)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

python tps/tp01/src/main.py
desactivate
cls
```

### Bash (Linux/macOS)

```bash
python3.12 -m venv .venv
source .venv/bin/activate
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

## Uso

```bash
python tps/tp01/src/main.py
```

## Entorno virtual (resumen)

1. Crear entorno (`venv`) una sola vez.
2. Activarlo según tu shell.
3. Instalar dependencias con `requirements.txt`.
4. Desactivarlo con `deactivate` al terminar.
