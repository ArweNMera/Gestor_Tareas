import tkinter as tk
from src.vista.gui_gestor_tareas import AplicacionGestorTareas

def main():
    root = tk.Tk()
    app = AplicacionGestorTareas(root)
    root.mainloop()

if __name__ == "__main__":
    main()