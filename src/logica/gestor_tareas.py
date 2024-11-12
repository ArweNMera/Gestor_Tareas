class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, descripcion):
        tarea = {
            'titulo': titulo,
            'descripcion': descripcion,
            'completada': False
        }
        self.tareas.append(tarea)
        return len(self.tareas) - 1

    def obtener_tareas(self):
        return self.tareas

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]['completada'] = True
            return True
        return False

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas.pop(indice)
            return True
        return False