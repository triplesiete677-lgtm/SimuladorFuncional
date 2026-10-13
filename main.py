import ttkbootstrap as ttk
from gui import ArenaApp

if __name__ == "__main__":
    app_root = ttk.Window(themename="darkly")
    app = ArenaApp(app_root)
    app_root.mainloop()