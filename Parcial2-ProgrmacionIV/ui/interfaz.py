# ui/interfaz.py
from crud.create import (
    crear_cliente, crear_factura, crear_control_plagas,
    crear_control_fertilizante, crear_antibiotico, buscar_por_cedula
)

def menu_principal():
    print("\n=== TIENDA AGRÍCOLA ===")
    print("1. Crear cliente")
    print("2. Crear factura")
    print("3. Crear producto")
    print("4. Agregar producto a factura")
    print("5. Buscar por cédula")
    print("6. Salir")
    return input("Seleccione una opción: ")

def ejecutar_ui():
    clientes = []
    productos = []  # Lista global de productos creados

    while True:
        opcion = menu_principal()

        # --- Crear cliente ---
        if opcion == "1":
            print("\n--- CREAR CLIENTE ---")
            nombre = input("Nombre del cliente: ")
            cedula = input("Cédula: ")
            cliente = crear_cliente(nombre, cedula)
            clientes.append(cliente)
            print("✅ Cliente creado exitosamente.\n")

        # --- Crear factura ---
        elif opcion == "2":
            print("\n--- CREAR FACTURA ---")
            if not clientes:
                print("⚠️ No hay clientes registrados. Cree uno primero.\n")
                continue

            print("Clientes registrados:")
            for c in clientes:
                print(f"- {c.nombre} (Cédula: {c.cedula})")

            cedula = input("Ingrese la cédula del cliente: ")
            cliente = next((c for c in clientes if c.cedula == cedula), None)
            if cliente:
                fecha = input("Fecha de la factura (YYYY-MM-DD): ")
                factura = crear_factura(cliente, fecha)
                print(f"✅ Factura creada para {cliente.nombre}.\n")
            else:
                print("⚠️ Cliente no encontrado.\n")

        # --- Crear producto ---
        elif opcion == "3":
            print("\n--- CREAR PRODUCTO ---")
            print("1. Control de Plagas")
            print("2. Control de Fertilizante")
            print("3. Antibiótico")
            tipo = input("Seleccione el tipo de producto: ")

            if tipo == "1":
                print("\nCreando producto tipo *Control de Plagas*")
                registro_ica = input("Registro ICA: ")
                nombre = input("Nombre: ")
                frecuencia = int(input("Frecuencia de aplicación (días): "))
                precio = float(input("Precio: "))
                periodo = int(input("Periodo de carencia (días): "))
                p = crear_control_plagas(registro_ica, nombre, frecuencia, precio, periodo)
                productos.append(p)
                print(f"✅ Producto '{p.nombre}' creado y agregado a la lista.\n")

            elif tipo == "2":
                print("\nCreando producto tipo *Control de Fertilizante*")
                registro_ica = input("Registro ICA: ")
                nombre = input("Nombre: ")
                frecuencia = int(input("Frecuencia de aplicación (días): "))
                precio = float(input("Precio: "))
                fecha_ultima = input("Fecha de última aplicación (YYYY-MM-DD): ")
                p = crear_control_fertilizante(registro_ica, nombre, frecuencia, precio, fecha_ultima)
                productos.append(p)
                print(f"✅ Producto '{p.nombre}' creado y agregado a la lista.\n")

            elif tipo == "3":
                print("\nCreando producto tipo *Antibiótico*")
                nombre = input("Nombre: ")
                print("Tipo de animal posible: bovino / caprino / porcino")
                tipo_animal = input("Tipo de animal: ").lower()
                dosis = int(input("Dosis (entre 400 y 600 Kg): "))
                precio = float(input("Precio: "))
                try:
                    p = crear_antibiotico(nombre, dosis, tipo_animal, precio)
                    productos.append(p)
                    print(f"✅ Antibiótico '{p.nombre}' creado y agregado a la lista.\n")
                except ValueError as e:
                    print(f"⚠️ Error: {e}\n")
            else:
                print("⚠️ Opción no válida.\n")

        # --- Agregar producto a factura ---
        elif opcion == "4":
            print("\n--- AGREGAR PRODUCTO A FACTURA ---")

            if not clientes:
                print("⚠️ No hay clientes registrados.\n")
                continue
            if not productos:
                print("⚠️ No hay productos creados.\n")
                continue

            cedula = input("Ingrese la cédula del cliente: ")
            cliente = next((c for c in clientes if c.cedula == cedula), None)
            if not cliente:
                print("⚠️ Cliente no encontrado.\n")
                continue

            if not cliente.facturas:
                print("⚠️ Este cliente no tiene facturas creadas.\n")
                continue

            print(f"\nFacturas del cliente {cliente.nombre}:")
            for i, f in enumerate(cliente.facturas):
                print(f"{i + 1}. Fecha: {f.fecha} | Total actual: ${f.total:.2f}")

            num_factura = int(input("Seleccione el número de factura: ")) - 1
            if num_factura < 0 or num_factura >= len(cliente.facturas):
                print("⚠️ Número de factura inválido.\n")
                continue

            factura = cliente.facturas[num_factura]

            print("\nProductos disponibles:")
            for i, p in enumerate(productos):
                print(f"{i + 1}. {p.nombre} (${p.precio:.2f})")

            num_producto = int(input("Seleccione el número del producto a agregar: ")) - 1
            if num_producto < 0 or num_producto >= len(productos):
                print("⚠️ Número de producto inválido.\n")
                continue

            producto = productos[num_producto]
            factura.agregar_producto(producto)
            print(f"✅ Producto '{producto.nombre}' agregado a la factura {factura.fecha}.\n")

        # --- Buscar por cédula ---
        elif opcion == "5":
            print("\n--- BUSCAR POR CÉDULA ---")
            if not clientes:
                print("⚠️ No hay clientes registrados.\n")
                continue

            cedula = input("Ingrese la cédula del cliente: ")
            buscar_por_cedula(clientes, cedula)

        # --- Salir del sistema ---
        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("⚠️ Opción no válida.\n")
