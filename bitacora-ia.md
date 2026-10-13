# Bitácora de Interacción con IA - Actividad Integradora (Unidades 1 y 2)

## 1. Información General
- **Proyecto:** Simulador de Arena de Combate / Gestor de Personajes Funcional (Python)
- **Herramienta de IA utilizada:** Asistente de IA (Gemini)
- **Propósito:** Apoyo en el diseño de la arquitectura modular, aplicación de conceptos funcionales avanzados (closures, funciones puras, inmutabilidad) y solución de errores de entorno.

---

## 2. Registro de Interacciones, Prompts y Decisiones

### Interacción 1: Estructuración inicial y separación de capas
- **Prompt del estudiante:** 
  > *"Ayúdame a hacer la actividad integradora de programación funcional unidades 1 y 2, que cumpla con dataclass, match/case, closures, funciones puras e impuras."*
- **Qué sugirió la IA:** 
  - Una estructura modular separando modelos de datos (`domain.py`), lógica pura (`logic.py`), interfaz gráfica (`gui.py`) y punto de entrada (`main.py`).
  - Uso de `@dataclass(frozen=True)` y `NamedTuple` para garantizar inmutabilidad.
  - Implementación de un closure real (`crear_multiplicador_danio`) y control de eventos con `match/case`.
- **Qué se aceptó:** 
  - Toda la arquitectura modular, la separación estricta entre la lógica pura y los efectos secundarios de la interfaz, y el uso del patrón `match/case` para procesar las acciones.
- **Qué se modificó / rechazó:** 
  - La IA sugirió inicialmente utilizar listas mutables (`.append()`) dentro de la estructura de estado para acumular el historial de eventos. 
  - **Por qué:** Se rechazó para cumplir rigurosamente con el principio de inmutabilidad de la programación funcional, reemplazando la lista por tuplas inmutables mediante concatenación (`estado.historial + (nuevo_evento,)`).

---

### Interacción 2: Resolución de dependencias y errores en el entorno
- **Prompt del estudiante:** 
  > *"Me sale este error en Pylance y en la terminal: ModuleNotFoundError: No module named 'ttkbootstrap'"*
- **Qué sugirió la IA:** 
  - Identificar que la librería gráfica externa `ttkbootstrap` no estaba instalada en el intérprete activo de Python dentro de VS Code.
  - Proveer el comando específico de instalación con la ruta completa del entorno actual de Python (`.../python.exe -m pip install ttkbootstrap`).
- **Qué se aceptó y modificó:** 
  - Se aceptó la solución y se ejecutó el comando de instalación en la terminal integrada, resolviendo los errores de importación y permitiendo la ejecución correcta de la interfaz gráfica.