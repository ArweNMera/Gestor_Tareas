import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.logica.gestor_tareas import GestorTareas


class AplicacionGestorTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')

        # Configurar el estilo
        self.configurar_estilo()

        self.gestor = GestorTareas()

        # Frame principal con fondo y bordes redondeados
        self.frame = ttk.Frame(root, padding="20", style='Card.TFrame')
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=20, pady=20)

        # Título de la aplicación
        titulo_app = ttk.Label(self.frame, text="✓ Gestor de Tareas",
                               style='Title.TLabel')
        titulo_app.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # Frame para el formulario
        form_frame = ttk.Frame(self.frame, style='Card.TFrame')
        form_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))

        # Campos de entrada con mejores estilos
        ttk.Label(form_frame, text="Título:", style='FieldLabel.TLabel').grid(
            row=0, column=0, sticky=tk.W, padx=(0, 10), pady=5)
        self.titulo_var = tk.StringVar()
        self.entrada_titulo = ttk.Entry(form_frame, textvariable=self.titulo_var,
                                        style='Custom.TEntry', width=40)
        self.entrada_titulo.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(form_frame, text="Descripción:", style='FieldLabel.TLabel').grid(
            row=1, column=0, sticky=tk.W, padx=(0, 10), pady=5)
        self.descripcion_var = tk.StringVar()
        self.entrada_descripcion = ttk.Entry(form_frame, textvariable=self.descripcion_var,
                                             style='Custom.TEntry', width=40)
        self.entrada_descripcion.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

        # Frame para botones
        button_frame = ttk.Frame(self.frame, style='Card.TFrame')
        button_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))

        # Botones con mejores estilos
        ttk.Button(button_frame, text="+ Agregar Tarea",
                   style='Primary.TButton', command=self.agregar_tarea).grid(
            row=0, column=0, padx=5)
        ttk.Button(button_frame, text="✓ Marcar Completada",
                   style='Success.TButton', command=self.marcar_completada).grid(
            row=0, column=1, padx=5)
        ttk.Button(button_frame, text="✗ Eliminar",
                   style='Danger.TButton', command=self.eliminar_tarea).grid(
            row=0, column=2, padx=5)

        # Lista de tareas con mejor estilo
        style = ttk.Style()
        style.configure("Custom.Treeview",
                        background="#ffffff",
                        foreground="black",
                        rowheight=30,
                        fieldbackground="#ffffff")
        style.configure("Custom.Treeview.Heading",
                        background="#f0f0f0",
                        foreground="black",
                        padding=5)

        # Frame para la lista con scroll
        list_frame = ttk.Frame(self.frame, style='Card.TFrame')
        list_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.lista_tareas = ttk.Treeview(list_frame, columns=('Título', 'Descripción', 'Estado'),
                                         style="Custom.Treeview", show='headings')
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.lista_tareas.yview)
        self.lista_tareas.configure(yscrollcommand=scrollbar.set)

        # Configurar columnas
        self.lista_tareas.heading('Título', text='Título')
        self.lista_tareas.heading('Descripción', text='Descripción')
        self.lista_tareas.heading('Estado', text='Estado')

        self.lista_tareas.column('Título', width=200)
        self.lista_tareas.column('Descripción', width=400)
        self.lista_tareas.column('Estado', width=100)

        # Colocar lista y scrollbar
        self.lista_tareas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # Hacer que la ventana y los frames sean expandibles
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(3, weight=1)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

    def configurar_estilo(self):
        style = ttk.Style()

        # Configurar colores y estilos generales
        style.configure('Card.TFrame', background='#ffffff', relief='flat')

        # Estilo para el título
        style.configure('Title.TLabel',
                        font=('Helvetica', 24, 'bold'),
                        foreground='#2c3e50',
                        background='#ffffff')

        # Estilo para etiquetas de campos
        style.configure('FieldLabel.TLabel',
                        font=('Helvetica', 10),
                        foreground='#34495e',
                        background='#ffffff')

        # Estilos para los botones
        style.configure('Primary.TButton',
                        font=('Helvetica', 10),
                        background='#3498db',
                        foreground='white')

        style.configure('Success.TButton',
                        font=('Helvetica', 10),
                        background='#2ecc71',
                        foreground='white')

        style.configure('Danger.TButton',
                        font=('Helvetica', 10),
                        background='#e74c3c',
                        foreground='white')

        # Estilo para los campos de entrada
        style.configure('Custom.TEntry',
                        padding=5,
                        relief='flat')

    def agregar_tarea(self):
        titulo = self.titulo_var.get()
        descripcion = self.descripcion_var.get()
        if titulo and descripcion:
            self.gestor.agregar_tarea(titulo, descripcion)
            self.actualizar_lista()
            self.titulo_var.set("")
            self.descripcion_var.set("")
        else:
            messagebox.showwarning("Error", "Por favor complete todos los campos",
                                   parent=self.root)

    def marcar_completada(self):
        seleccion = self.lista_tareas.selection()
        if seleccion:
            indice = self.lista_tareas.index(seleccion[0])
            if self.gestor.marcar_completada(indice):
                self.actualizar_lista()

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.selection()
        if seleccion:
            if messagebox.askyesno("Confirmar eliminación",
                                   "¿Está seguro de que desea eliminar esta tarea?",
                                   parent=self.root):
                indice = self.lista_tareas.index(seleccion[0])
                if self.gestor.eliminar_tarea(indice):
                    self.actualizar_lista()

    def actualizar_lista(self):
        for item in self.lista_tareas.get_children():
            self.lista_tareas.delete(item)

        for i, tarea in enumerate(self.gestor.obtener_tareas()):
            estado = "✓ Completada" if tarea['completada'] else "Pendiente"
            self.lista_tareas.insert('', 'end', values=(tarea['titulo'],
                                                        tarea['descripcion'],
                                                        estado))
            if tarea['completada']:
                item = self.lista_tareas.get_children()[-1]
                self.lista_tareas.tag_configure('completed', foreground='#27ae60')
                self.lista_tareas.item(item, tags=('completed',))