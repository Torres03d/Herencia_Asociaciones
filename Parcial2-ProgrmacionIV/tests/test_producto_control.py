# tests/test_producto_control.py
import unittest
from modelo.control_plagas import ControlPlagas
from modelo.control_fertilizante import ControlFertilizante

class TestProductoControl(unittest.TestCase):
    def test_crear_control_plagas(self):
        p = ControlPlagas("ICA111", "PlaguicidaY", 15, 7000, 8)
        self.assertEqual(p.nombre, "PlaguicidaY")
        self.assertEqual(p.periodo_carencia, 8)

    def test_crear_control_fertilizante(self):
        f = ControlFertilizante("ICA222", "AbonoPlus", 30, 9000, "2025-09-20")
        self.assertEqual(f.frecuencia_aplicacion, 30)
        self.assertEqual(f.fecha_ultima_aplicacion, "2025-09-20")

if __name__ == "__main__":
    unittest.main()
