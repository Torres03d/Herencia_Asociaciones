# tests/test_cliente.py
import unittest
from modelo.cliente import Cliente
from modelo.factura import Factura

class TestCliente(unittest.TestCase):
    def test_agregar_factura(self):
        cliente = Cliente("Juan", "123")
        factura = Factura("2025-11-01", cliente)
        self.assertIn(factura, cliente.facturas)
        self.assertEqual(len(cliente.facturas), 1)

if __name__ == "__main__":
    unittest.main()
