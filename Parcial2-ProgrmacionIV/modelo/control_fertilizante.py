# modelo/control_fertilizante.py
from modelo.producto_control import ProductoControl

class ControlFertilizante(ProductoControl):
    def __init__(self, registro_ica, nombre, frecuencia_aplicacion, precio, fecha_ultima_aplicacion):
        """Control de fertilizantes, con fecha de última aplicación adicional."""
        super().__init__(registro_ica, nombre, frecuencia_aplicacion, precio)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion
