import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.logica.gestor_tareas import GestorTareas


class TestGestorTareas(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorTareas()

    def test_agregar_tarea(self):
        indice = self.gestor.agregar_tarea("Test", "Descripción test")
        self.assertEqual(indice, 0)
        self.assertEqual(len(self.gestor.tareas), 1)
        self.assertEqual(self.gestor.tareas[0]['titulo'], "Test")

    def test_marcar_completada(self):
        self.gestor.agregar_tarea("Test", "Descripción test")
        resultado = self.gestor.marcar_completada(0)
        self.assertTrue(resultado)
        self.assertTrue(self.gestor.tareas[0]['completada'])

    def test_eliminar_tarea(self):
        self.gestor.agregar_tarea("Test", "Descripción test")
        resultado = self.gestor.eliminar_tarea(0)
        self.assertTrue(resultado)
        self.assertEqual(len(self.gestor.tareas), 0)


if __name__ == '__main__':
    unittest.main()