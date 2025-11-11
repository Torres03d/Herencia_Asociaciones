# crud/create.py
from modelo.cliente import Cliente
from modelo.factura import Factura
from modelo.control_plagas import ControlPlagas
from modelo.control_fertilizante import ControlFertilizante
from modelo.antibiotico import Antibiotico

# Funciones de creación (ya existentes)
def crear_cliente(nombre, cedula):
    return Cliente(nombre, cedula)

def crear_factura(cliente, fecha):
    factura = Factura(fecha, cliente)
    cliente.agregar_factura(factura)
    return factura

def crear_control_plagas(registro_ica, nombre, frecuencia_aplicacion, precio, periodo_carencia):
    return ControlPlagas(registro_ica, nombre, frecuencia_aplicacion, precio, periodo_carencia)

def crear_control_fertilizante(registro_ica, nombre, frecuencia_aplicacion, precio, fecha_ultima_aplicacion):
    return ControlFertilizante(registro_ica, nombre, frecuencia_aplicacion, precio, fecha_ultima_aplicacion)

def crear_antibiotico(nombre, dosis, tipo_animal, precio):
    return Antibiotico(nombre, dosis, tipo_animal, precio)


# 🔍 Nueva función requerida por el proyecto
def buscar_por_cedula(clientes, cedula):
    """
    Busca un cliente por cédula y muestra todas las facturas asociadas,
    junto con los productos vendidos en cada factura.
    """
    cliente = next((c for c in clientes if c.cedula == cedula), None)
    if not cliente:
        print(f"⚠️ No se encontró ningún cliente con cédula {cedula}.")
        return

    print(f"\n📄 Facturas del cliente {cliente.nombre} (Cédula: {cliente.cedula})")
    if not cliente.facturas:
        print("   No tiene facturas registradas.\n")
        return

    for factura in cliente.facturas:
        print(f"\n  🧾 Fecha: {factura.fecha}")
        print(f"  Total: ${factura.total:.2f}")
        if not factura.productos:
            print("   Sin productos registrados.")
        else:
            print("   Productos vendidos:")
            for p in factura.productos:
                print(f"    - {p.nombre} (${p.precio:.2f})")
    print()
