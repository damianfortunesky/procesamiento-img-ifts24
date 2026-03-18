TAREA
Inicializar repositorio base para trabajos prácticos de Procesamiento de Imágenes Digitales con Python 3 y py5

CONTEXTO
- Proyecto: Repositorio académico para almacenar y desarrollar los TPs de la materia Procesamiento de Imágenes Digitales
- Stack: Visual Studio Code, Python 3, py5
- Arquitectura: repositorio monolítico simple orientado a múltiples trabajos prácticos
- Módulo afectado: estructura base del repositorio
- Rama/base: main
- Restricciones técnicas relevantes:
  - Aún no están definidas las especificaciones funcionales de cada TP
  - La estructura debe permitir agregar nuevos TPs sin reorganizar el repositorio
  - Evitar sobreingeniería
  - Mantener compatibilidad simple con ejecución local desde VS Code
  - No asumir frameworks adicionales aparte de Python 3 y py5

OBJETIVO
Crear la base inicial del repositorio para soportar el desarrollo incremental de los trabajos prácticos, dejando una estructura clara, mantenible y lista para incorporar futuras consignas sin necesidad de refactorizaciones grandes.

ALCANCE
Sí:
- Inicializar proyecto en Python para la materia "Procesamiento de Imágenes Digitales"
- Definir una estructura de carpetas simple y escalable para múltiples TPs
- Agregar un README inicial con propósito del repositorio, requisitos y forma de uso
- Agregar archivo de dependencias o mecanismo básico de instalación del entorno
- Agregar `.gitignore` adecuado para Python y VS Code
- Crear al menos un TP de ejemplo vacío o base (`tp01`) con punto de entrada mínimo
- Dejar preparado un espacio para assets/imagenes de entrada y salida por TP
- Mantener el proyecto listo para abrir y trabajar desde VS Code

No:
- Implementar lógica específica de procesamiento de imágenes de un TP real
- Definir algoritmos, filtros o transformaciones que aún no fueron solicitados
- Agregar frameworks o librerías extra no necesarias
- Diseñar una arquitectura compleja por capas
- Automatizar CI/CD o pipelines en esta etapa

REGLAS DE IMPLEMENTACIÓN
- Mantener consistencia con un estilo académico/técnico simple y profesional.
- Hacer el cambio más simple posible.
- No introducir dependencias nuevas salvo justificación explícita.
- No refactorizar partes no relacionadas.
- Elegir la opción de menor impacto cuando existan varias alternativas válidas.
- Priorizar una estructura entendible para futuros TPs.
- Usar nombres de carpetas y archivos claros y predecibles.
- Dejar comentarios solo cuando aporten contexto real.

CRITERIOS DE ACEPTACIÓN
- Existe una estructura base funcional para alojar múltiples TPs
- El repositorio incluye README con instrucciones mínimas de instalación y ejecución
- Existe un `.gitignore` apropiado para Python/VS Code
- Existe una forma clara de instalar dependencias del proyecto
- Existe un directorio inicial para un primer TP (`tp01` o equivalente)
- El TP inicial tiene un archivo base ejecutable o stub preparado para comenzar desarrollo
- La estructura contempla entrada/salida de imágenes de forma ordenada
- La organización propuesta no depende de conocer aún el detalle de cada consigna

VALIDACIÓN
- Verificar que el repositorio pueda abrirse correctamente en VS Code
- Verificar que la estructura creada sea consistente y navegable
- Verificar que los archivos base estén correctamente referenciados en la documentación
- Si se agrega un punto de entrada inicial, indicar cómo ejecutarlo
- Si algo no pudo validarse, indicarlo explícitamente
- No reportar tests como exitosos si no se ejecutaron

ENTREGABLE ESPERADO
- Resumen breve del enfoque
- Archivos creados/modificados
- Estructura propuesta del repositorio
- Cambios realizados
- Riesgos o puntos a revisar