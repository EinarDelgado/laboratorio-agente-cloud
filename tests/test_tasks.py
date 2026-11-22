import unittest
from tasks import agregar_tarea, completar_tarea, pendientes


class TestTasks(unittest.TestCase):
    def test_agregar_tarea(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación")
        self.assertEqual(tarea["titulo"], "Leer documentación")
        self.assertFalse(tarea["completada"])

    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar")
        completar_tarea(tareas, 1)
        self.assertEqual(pendientes(tareas), [])


class TestCategorias(unittest.TestCase):
    def setUp(self):
        self.tareas = []
        agregar_tarea(self.tareas, "Estudiar", "Universidad")
        agregar_tarea(self.tareas, "Comprar pan", "Personal")
        agregar_tarea(self.tareas, "Entregar informe", "universidad")

    def test_categoria_valida_se_guarda(self):
        self.assertEqual(self.tareas[0]["categoria"], "Universidad")

    def test_categoria_vacia_lanza_value_error(self):
        for categoria in ("", "   "):
            with self.subTest(categoria=categoria):
                with self.assertRaises(ValueError):
                    agregar_tarea(self.tareas, "Tarea", categoria)
        self.assertEqual(len(self.tareas), 3)

    def test_filtrar_pendientes_sin_distinguir_mayusculas(self):
        resultado = pendientes(self.tareas, "UNIVERSIDAD")
        self.assertEqual([t["id"] for t in resultado], [1, 3])

    def test_filtrar_excluye_completadas(self):
        completar_tarea(self.tareas, 1)
        self.assertEqual([t["id"] for t in pendientes(self.tareas, "universidad")], [3])

    def test_sin_categoria_devuelve_todas_las_pendientes(self):
        self.assertEqual(len(pendientes(self.tareas)), 3)


if __name__ == "__main__":
    unittest.main()
