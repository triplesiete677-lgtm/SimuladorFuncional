from functools import reduce
from domain import Personaje, EstadoJuego, Habilidad

def crear_multiplicador_danio(factor: float):
    def calcular(danio_base: int) -> int:
        return int(danio_base * factor)
    return calcular

buff_critico = crear_multiplicador_danio(1.5)
buff_debilidad = crear_multiplicador_danio(0.8)

def aplicar_danio(defensor: Personaje, cantidad: int) -> Personaje:
    dano_real = max(cantidad - defensor.escudo, 0)
    nueva_vida = max(defensor.vida - dano_real, 0)
    return Personaje(
        nombre=defensor.nombre,
        clase=defensor.clase,
        vida=nueva_vida,
        vida_maxima=defensor.vida_maxima,
        ataque=defensor.ataque,
        escudo=max(0, defensor.escudo - cantidad)
    )

def aplicar_curacion(personaje: Personaje, cantidad: int) -> Personaje:
    nueva_vida = min(personaje.vida_maxima, personaje.vida + cantidad)
    return Personaje(
        nombre=personaje.nombre,
        clase=personaje.clase,
        vida=nueva_vida,
        vida_maxima=personaje.vida_maxima,
        ataque=personaje.ataque,
        escudo=personaje.escudo
    )

def procesar_accion(estado: EstadoJuego, accion: str) -> EstadoJuego:
    # Si el juego ya terminó (alguien murió), no permitimos más acciones
    if estado.jugador.vida <= 0 or estado.enemigo.vida <= 0:
        return estado

    match accion:
        case "atacar":
            # 1. Turno del Jugador
            danio = buff_critico(estado.jugador.ataque)
            enemigo_post_ataque = aplicar_danio(estado.enemigo, danio)
            historial = estado.historial + (f"Atacaste infligiendo {danio} de daño.",)
            
            # Verificar si el enemigo murió
            if enemigo_post_ataque.vida <= 0:
                historial += ("¡Has derrotado al monstruo! ¡Victoria!",)
                return EstadoJuego(estado.jugador, enemigo_post_ataque, historial)

            # 2. Contraataque del Monstruo (Turno enemigo)
            danio_enemigo = estado.enemigo.ataque
            jugador_post_contra = aplicar_danio(estado.jugador, danio_enemigo)
            historial += (f"El monstruo contraataca y te inflige {danio_enemigo} de daño.",)

            if jugador_post_contra.vida <= 0:
                historial += ("¡Has sido derrotado! Fin del juego.",)

            return EstadoJuego(jugador_post_contra, enemigo_post_ataque, historial)

        case "curar":
            jugador_post_cura = aplicar_curacion(estado.jugador, 25)
            historial = estado.historial + ("Te curaste 25 puntos de vida.",)

            # Contraataque del Monstruo tras curarse
            danio_enemigo = estado.enemigo.ataque
            jugador_post_contra = aplicar_danio(jugador_post_cura, danio_enemigo)
            historial += (f"El monstruo aprovecha y te inflige {danio_enemigo} de daño.",)

            if jugador_post_contra.vida <= 0:
                historial += ("¡Has sido derrotado! Fin del juego.",)

            return EstadoJuego(jugador_post_contra, estado.enemigo, historial)

        case "escudo":
            jugador_post_escudo = Personaje(
                nombre=estado.jugador.nombre,
                clase=estado.jugador.clase,
                vida=estado.jugador.vida,
                vida_maxima=estado.jugador.vida_maxima,
                ataque=estado.jugador.ataque,
                escudo=estado.jugador.escudo + 15
            )
            historial = estado.historial + ("Aumentaste tu escudo en 15 puntos.",)

            # Contraataque del Monstruo
            danio_enemigo = estado.enemigo.ataque
            jugador_post_contra = aplicar_danio(jugador_post_escudo, danio_enemigo)
            historial += (f"El monstruo ataca tu escudo y te inflige daño.",)

            if jugador_post_contra.vida <= 0:
                historial += ("¡Has sido derrotado! Fin del juego.",)

            return EstadoJuego(jugador_post_contra, estado.enemigo, historial)

        case _:
            return estado

def filtrar_eventos_importantes(historial: tuple, palabra_clave: str) -> list:
    return list(filter(lambda log: palabra_clave in log.lower(), historial))

def calcular_salud_total_combate(personajes: list) -> int:
    return reduce(lambda acc, p: acc + p.vida, personajes, 0)