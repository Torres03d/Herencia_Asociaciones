# modelo/factura.py
class Factura:
    def __init__(self, fecha, cliente=None):
        """
        Factura con fecha, lista de productos y valor total calculado.
        Si se proporciona un cliente, la factura se añade a dicho cliente.
        """
        self.fecha = fecha
        self.productos = []
        self.total = 0
        self.cliente = cliente
        if cliente is not None:
            cliente.agregar_factura(self)

    def agregar_producto(self, producto):
        """Agrega un producto (cualquier subclase) y actualiza el total de la factura."""
        self.productos.append(producto)
        self.total += producto.precio
