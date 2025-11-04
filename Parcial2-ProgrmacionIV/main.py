# main.py
from modelo.cliente import Cliente
from modelo.factura import Factura
from modelo.control_plagas import ControlPlagas
from modelo.control_fertilizante import ControlFertilizante
from modelo.antibiotico import Antibiotico

if __name__ == "__main__":
    # Crear algunos clientes
    cliente1 = Cliente("María Gómez", "89123456")
    cliente2 = Cliente("Carlos Pérez", "90876543")

    # Crear facturas para cada cliente
    factura1 = Factura("2025-10-01", cliente1)
    factura2 = Factura("2025-10-02", cliente1)
    factura3 = Factura("2025-10-01", cliente2)

    # Crear productos de control
    plaga = ControlPlagas(registro_ica="ICA001", nombre="Fosfitop", frecuencia_aplicacion=15, precio=5000.0, periodo_carencia=7)
    ferti = ControlFertilizante(registro_ica="ICA002", nombre="FertiMax", frecuencia_aplicacion=30, precio=8000.0, fecha_ultima_aplicacion="2025-09-15")
    # Crear antibióticos
    anti1 = Antibiotico(nombre="Oxitetraciclina", dosis=500, tipo_animal="bovino", precio=12000.0)
    anti2 = Antibiotico(nombre="Penicilina", dosis=450, tipo_animal="porcino", precio=15000.0)

    # Agregar productos a facturas
    factura1.agregar_producto(plaga)
    factura1.agregar_producto(anti1)

    factura2.agregar_producto(ferti)
    factura2.agregar_producto(anti1)
    factura2.agregar_producto(anti2)

    factura3.agregar_producto(plaga)
    factura3.agregar_producto(ferti)

    # Mostrar facturación por cliente
    for cliente in [cliente1, cliente2]:
        print(f"Cliente: {cliente.nombre} (Cédula {cliente.cedula})")
        for factura in cliente.facturas:
            print(f"  Factura {factura.fecha}: Total = ${factura.total:.2f}")
            for prod in factura.productos:
                print(f"    - {prod.nombre} (${prod.precio:.2f})")
        print()
