# modelo/producto_control.py
class ProductoControl:
    def __init__(self, registro_ica, nombre, frecuencia_aplicacion, precio):
        """Producto de control genérico con registro ICA, nombre, frecuencia de aplicación (días) y precio."""
        self.registro_ica = registro_ica
        self.nombre = nombre
        self.frecuencia_aplicacion = frecuencia_aplicacion
        self.precio = precio
