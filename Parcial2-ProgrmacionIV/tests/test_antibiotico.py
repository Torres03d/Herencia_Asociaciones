# tests/test_antibiotico.py
import unittest
from modelo.antibiotico import Antibiotico

class TestAntibiotico(unittest.TestCase):
    def test_crear_antibiotico_valido(self):
        a = Antibiotico("Penicilina", 500, "porcino", 15000)
        self.assertEqual(a.nombre, "Penicilina")
        self.assertEqual(a.tipo_animal, "porcino")

    def test_dosis_fuera_de_rango(self):
        with self.assertRaises(ValueError):
            Antibiotico("Tetra", 300, "bovino", 10000)

    def test_tipo_animal_invalido(self):
        with self.assertRaises(ValueError):
            Antibiotico("Amoxi", 500, "gato", 8000)

if __name__ == "__main__":
    unittest.main()
