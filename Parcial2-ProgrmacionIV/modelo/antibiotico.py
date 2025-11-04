# modelo/antibiotico.py
class Antibiotico:
    def __init__(self, nombre, dosis, tipo_animal, precio):
        """
        Antibiótico para animales de granja.
        - dosis (kg): debe estar entre 400 y 600 (inclusive).
        - tipo_animal: 'bovino', 'caprino' o 'porcino'.
        """
        if dosis < 400 or dosis > 600:
            raise ValueError("Dosis debe estar entre 400Kg y 600Kg")
        if tipo_animal.lower() not in ("bovino", "caprino", "porcino"):
            raise ValueError("Tipo de animal debe ser 'bovino', 'caprino' o 'porcino'")
        self.nombre = nombre
        self.dosis = dosis
        self.tipo_animal = tipo_animal
        self.precio = precio
