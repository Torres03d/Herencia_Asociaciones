# test/test_relaciones.py
import unittest
from modelo.cliente import Cliente
from modelo.factura import Factura
from modelo.control_plagas import ControlPlagas
from modelo.control_fertilizante import ControlFertilizante
from modelo.antibiotico import Antibiotico

class TestRelacionesYHerencia(unittest.TestCase):
    def test_asociacion_cliente_factura(self):
        cliente = Cliente("Laura", "1001")
        factura = Factura("2025-10-10", cliente)
        cliente.agregar_factura(factura)
        self.assertIn(factura, cliente.facturas)
        print(f"\n🔗 Asociación verificada: {cliente.nombre} tiene {len(cliente.facturas)} factura(s).")

    def test_asociacion_factura_productos(self):
        cliente = Cliente("Pedro", "2002")
        factura = Factura("2025-10-11", cliente)
        producto1 = ControlPlagas("ICA100", "Insectox", 15, 5000, 7)
        producto2 = Antibiotico("Amoxicilina", 500, "bovino", 10000)
        factura.agregar_producto(producto1)
        factura.agregar_producto(producto2)
        self.assertEqual(len(factura.productos), 2)
        print(f"🧾 Factura asociada con {len(factura.productos)} productos.")

    def test_herencia_productos_control(self):
        plaga = ControlPlagas("ICA101", "Plagox", 30, 6000, 10)
        ferti = ControlFertilizante("ICA102", "Fertimax", 15, 8000, "2025-09-10")

        # Verificar que son instancias de la clase padre
        from modelo.producto_control import ProductoControl
        self.assertIsInstance(plaga, ProductoControl)
        self.assertIsInstance(ferti, ProductoControl)
        print("🧬 Herencia verificada: ControlPlagas y ControlFertilizante heredan de ProductoControl.")

if __name__ == "__main__":
    unittest.main()
