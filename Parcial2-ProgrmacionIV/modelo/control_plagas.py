# modelo/control_plagas.py
from modelo.producto_control import ProductoControl

class ControlPlagas(ProductoControl):
    def __init__(self, registro_ica, nombre, frecuencia_aplicacion, precio, periodo_carencia):
        """Control de plagas, con período de carencia adicional (días)."""
        super().__init__(registro_ica, nombre, frecuencia_aplicacion, precio)
        self.periodo_carencia = periodo_carencia
