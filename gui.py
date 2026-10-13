import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from domain import Personaje, EstadoJuego
from logic import procesar_accion

class ArenaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Arena Funcional - RPG Simulator")
        self.root.geometry("600x580")

        # Estado inicial inmutable
        p1 = Personaje("Héroe", "Guerrero", 100, 100, 20, 0)
        p2 = Personaje("Monstruo", "Orco", 120, 120, 15, 0)
        self.estado = EstadoJuego(jugador=p1, enemigo=p2, historial=())

        self._crear_interfaz()
        self._actualizar_pantalla()

    def _crear_interfaz(self):
        lbl_titulo = ttk.Label(self.root, text="Simulador de Arena Funcional", font=("Helvetica", 16, "bold"))
        lbl_titulo.pack(pady=10)

        self.frame_stats = ttk.Frame(self.root, padding=10)
        self.frame_stats.pack(fill=X, padx=20)

        self.lbl_jugador = ttk.Label(self.frame_stats, text="", font=("Helvetica", 10))
        self.lbl_jugador.pack(anchor=W)

        self.lbl_enemigo = ttk.Label(self.frame_stats, text="", font=("Helvetica", 10))
        self.lbl_enemigo.pack(anchor=W)

        frame_botones = ttk.Frame(self.root, padding=10)
        frame_botones.pack(pady=10)

        # Guardamos los botones como atributos para poder desactivarlos si termina la partida
        self.btn_atacar = ttk.Button(frame_botones, text="Atacar", bootstyle=DANGER, command=lambda: self._ejecutar("atacar"))
        self.btn_atacar.grid(row=0, column=0, padx=5)

        self.btn_curar = ttk.Button(frame_botones, text="Curar", bootstyle=SUCCESS, command=lambda: self._ejecutar("curar"))
        self.btn_curar.grid(row=0, column=1, padx=5)

        self.btn_escudo = ttk.Button(frame_botones, text="Escudo", bootstyle=INFO, command=lambda: self._ejecutar("escudo"))
        self.btn_escudo.grid(row=0, column=2, padx=5)

        self.txt_historial = ttk.ScrolledText(self.root, height=12, width=65)
        self.txt_historial.pack(padx=20, pady=10)

    def _ejecutar(self, accion: str):
        self.estado = procesar_accion(self.estado, accion)
        self._actualizar_pantalla()

    def _actualizar_pantalla(self):
        j = self.estado.jugador
        e = self.estado.enemigo

        self.lbl_jugador.config(text=f"Jugador: {j.nombre} | HP: {j.vida}/{j.vida_maxima} | Escudo: {j.escudo}")
        self.lbl_enemigo.config(text=f"Enemigo: {e.nombre} | HP: {e.vida}/{e.vida_maxima} | Escudo: {e.escudo}")

        self.txt_historial.delete("1.0", END)
        for log in self.estado.historial:
            self.txt_historial.insert(END, f"> {log}\n")
        
        # Desactivar botones si la partida terminó (alguien murió)
        if j.vida <= 0 or e.vida <= 0:
            self.btn_atacar.config(state="disabled")
            self.btn_curar.config(state="disabled")
            self.btn_escudo.config(state="disabled")