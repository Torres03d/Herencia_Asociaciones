# modelo/cliente.py
class Cliente:
    def __init__(self, nombre, cedula):
        """Cliente con nombre, cédula y lista de facturas asociadas."""
        self.nombre = nombre
        self.cedula = cedula
        self.facturas = []

    def agregar_factura(self, factura):
        """Asocia una Factura a este cliente (composición Cliente tiene Facturas)."""
        self.facturas.append(factura)
