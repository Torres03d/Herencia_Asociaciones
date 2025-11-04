# tests/test_factura.py
import unittest
from modelo.cliente import Cliente
from modelo.factura import Factura
from modelo.control_plagas import ControlPlagas
from modelo.control_fertilizante import ControlFertilizante
from modelo.antibiotico import Antibiotico

class TestFactura(unittest.TestCase):
    def test_agregar_producto_actualiza_total(self):
        cliente = Cliente("Ana", "456")
        factura = Factura("2025-11-01", cliente)
        plaga = ControlPlagas("ICA100", "PlaguicidaX", 15, 5000, 7)
        factura.agregar_producto(plaga)
        self.assertEqual(factura.total, 5000)

    def test_factura_con_varios_productos(self):
        cliente = Cliente("Pedro", "789")
        factura = Factura("2025-11-02", cliente)
        p1 = ControlPlagas("ICA200", "Fosfitop", 15, 5000, 10)
        p2 = ControlFertilizante("ICA201", "FertiMax", 30, 8000, "2025-09-15")
        p3 = Antibiotico("Oxitetraciclina", 500, "bovino", 12000)
        factura.agregar_producto(p1)
        factura.agregar_producto(p2)
        factura.agregar_producto(p3)
        self.assertEqual(factura.total, 5000 + 8000 + 12000)

if __name__ == "__main__":
    unittest.main()
