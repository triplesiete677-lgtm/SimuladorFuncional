from dataclasses import dataclass
from typing import NamedTuple, Union

class Habilidad(NamedTuple):
    nombre: str
    poder: int
    tipo: str

@dataclass(frozen=True)
class Personaje:
    nombre: str
    clase: str
    vida: int
    vida_maxima: int
    ataque: int
    escudo : int
    
@dataclass(frozen=True)
class EstadoJuego:
    jugador: Personaje
    enemigo: Personaje
    historial: tuple