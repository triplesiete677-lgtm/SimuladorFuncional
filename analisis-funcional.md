# Análisis de Implementación Funcional

## 1. Problema que resuelve
Un simulador interactivo de arena de combate RPG que gestiona estados de personajes, cálculo de daño, habilidades y registro de eventos asegurando trazabilidad sin mutación directa de datos.

## 2. Estructuras de datos utilizadas
- `NamedTuple`: Utilizado en `Habilidad` para inmutabilidad con acceso rápido.
- `@dataclass(frozen=True)`: Utilizado en `Personaje` y `EstadoJuego` para forzar que los atributos sean inmutables.

## 3. Justificación de Conceptos Aplicados

### Unidad 1
- **Match / Case**: Implementado en `procesar_accion()` dentro de `logic.py` para desacoplar el dispatching de eventos de la interfaz de usuario.
- **Modelado de Datos**: `dataclass` con `frozen=True` previene efectos secundarios indeseados sobre los atributos.

### Unidad 2
- **Closure**: La función `crear_multiplicador_danio(factor)` genera funciones derivadas personalizadas (`buff_critico`, `buff_debilidad`) manteniendo el estado encapsulado en su scope léxico.
- **Inmutabilidad**: Toda modificación al estado del juego genera una nueva instancia del objeto `EstadoJuego`.
- **Pureza y Efectos Secundarios**:
  - *Funciones Puras*: `aplicar_danio()`, `aplicar_curacion()`, `procesar_accion()`. Reciben entradas y retornan salidas deterministas sin alterar variables externas.
  - *Funciones Impuras (Efectos secundarios)*: `_ejecutar()` y `_actualizar_pantalla()` en `gui.py`. Son requeridas para interactuar con el usuario, actualizar el DOM/Widgets de Tkinter e imprimir eventos.
- **Map / Filter / Reduce**: Uso de `filter()` en `filtrar_eventos_importantes()` para búsquedas en el historial e iteraciones sobre colecciones tuple.

## 4. Fragmento donde no conviene usar lambda
En la función `procesar_accion` no se utilizó `lambda` debido a que maneja múltiples flujos lógicos con `match/case` y reestructuración de clases. Usar `lambda` aquí reduciría drásticamente la legibilidad y violaría el principio de responsabilidad única.

## 5. Auditoría y Criterio de uso de IA
- **Sugerido por IA**: La plantilla base de `ttkbootstrap` y la estructura inicial de la interfaz de Tkinter.
- **Corregido/Rechazado**: La IA sugirió originalmente mutar la lista de historial con `.append()` dentro del objeto `EstadoJuego`. Fue rechazado para mantener la inmutabilidad utilizando tuplas (`tuple`) y concatenación pura.