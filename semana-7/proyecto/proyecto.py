import time

def pantalla_carga():
    
    print("\n[SISTEMA] Iniciando programa...")

    for segundo in range(1, 6):
        print(f"Cargando entorno... {segundo}/5 segundos")
        time.sleep(1)
    print("Sistema cargado con éxito\n")

def gestionar_usuarios():
    
    archivo_usuarios = "usuarios.txt"
    
    try:
        with open(archivo_usuarios, "r") as f:
            usuarios_registrados = f.read().splitlines()
    except FileNotFoundError:  
        with open(archivo_usuarios, "w") as f:
            usuarios_registrados = []

    print("="*40)
    print("  ACCESO DE USUARIOS  ")
    print("="*40)
    print("1. Iniciar sesion")
    print("2. Registrar nueva cuenta")

    opcion = input("Seleccione una opción (1 o 2): ")

    if opcion == "1":
        
        usuario = input("Ingrese su nombre de usuario: ")

        if usuario in usuarios_registrados:
            print(f"\nBienvenido de nuevo, {usuario}.")
            return usuario

        else:
            print("\nEl usuario no esta registrado. Intente de nuevo o registrese.")
            return gestionar_usuarios()
            
    elif opcion == "2":

        nuevo_usuario = input("Elija un nombre de usuario nuevo: ")

        if nuevo_usuario in usuarios_registrados:
            print("\nEse usuario ya existe. Intente iniciar sesión.")
            return gestionar_usuarios()

        else:

            with open(archivo_usuarios, "a") as f:
                f.write(nuevo_usuario + "\n")
            print(f"\nCuenta creada y guardada con exito, bienvenido, {nuevo_usuario}.")
            return nuevo_usuario

    else:
        print("Opción invalida.")
        return gestionar_usuarios()

def capturar_fecha():

    print("\n--- CAPTURA DE FECHA DE OPERACIÓN ---")

    dia = input("Ingrese el día (ej. 12): ")
    mes = input("Ingrese el mes (ej. 06): ")
    anio = input("Ingrese el año (ej. 2026): ")
    Fecha = (dia, mes, anio)

    print(f"Fecha registrada: {Fecha[0]}/{Fecha[1]}/{Fecha[2]}")

    return Fecha

def taqueria_pedidos(fecha_actual):

    total_dia = 0
    num_pedidos = 0
    continuar_cliente = "si"
    
    while continuar_cliente.lower() == "si":

        print("====================================")
        print("     TAQUERÍA LAS BRASAS DE OAXACA  ")
        print("====================================")
        
        try:
            numero_mesa = int(input("Ingrese el número de mesa: "))
        except ValueError:
            print("Número de mesa inválido.")
            continue
            
        subtotal = 0
        opcion = 0
        
        while opcion != 6:
            print("\n--- MENÚ DE PLATILLOS ---")
            print("1. Orden Tacos al Pastor (3 pzs) - $60")
            print("2. Orden Quesadillas Oaxaqueñas (2 pzs) - $50")
            print("3. Alambre Especial de la Casa - $110")
            print("4. Agua Fresca (1 L) - $30")
            print("5. Refresco (600 ml) - $25")
            print("6. Finalizar pedido de la mesa")
            
            try:
                opcion = int(input("Seleccione una opción (1-6): "))
            except ValueError:
                print("Opción inválida.")
                continue
                
            if 1 <= opcion <= 5:
                try:
                    cantidad = int(input("Ingrese la cantidad solicitada: "))
                except ValueError:
                    print("Cantidad inválida.")
                    continue
                    
                if cantidad > 0:
                    cargoextra = 0
                    precio = 0
                    
                    if opcion == 1:
                        precio = 60
                        if cantidad == 1:
                            resp = input("¿Desea 1 pieza individual? (s/n): ").lower()
                            if resp == "s":
                                precio = 25
                                cargoextra = 10
                    elif opcion == 2:
                        precio = 50
                        if cantidad == 1:
                            resp = input("¿Desea 1 pieza individual? (s/n): ").lower()
                            if resp == "s":
                                precio = 35
                                cargoextra = 10
                    elif opcion == 3:
                        precio = 110
                    elif opcion == 4:
                        precio = 30
                    elif opcion == 5:
                        precio = 25
                            
                    subtotal += (precio * cantidad)
                    if cargoextra > 0:
                        subtotal += cargoextra
                        print("-> Se aplicó un cargo extra de $10.00 MXN.")
                    print(f"-> Subtotal mesa: ${subtotal}")
                else:
                    print("La cantidad debe ser mayor a 0.")
            elif opcion == 6:
                break
            else:
                print("Opción inválida.")
                
        if subtotal > 0:
            total_pedido = subtotal
            total_dia += total_pedido
            num_pedidos += 1
            
            print(f"\nRESUMEN MESA {numero_mesa} | Total: ${total_pedido}")
            
            nombre_archivo = f"ventas_{fecha_actual[0]}_{fecha_actual[1]}_{fecha_actual[2]}.txt"

            with open(nombre_archivo, "a") as archivo:
                archivo.write(f"Fecha: {fecha_actual[0]}/{fecha_actual[1]}/{fecha_actual[2]} | Mesa: {numero_mesa} | Total: ${total_pedido}\n")

            print(f"-> Venta guardada en '{nombre_archivo}'.")
            
        else:
            print("Pedido cancelado o sin ítems.")
            
        continuar_cliente = input("¿Desea atender a otra mesa? (si/no): ")
        
    print(f"\n--- CORTE DEL DÍA ---\nMesas atendidas: {num_pedidos} | Ventas totales: ${total_dia}")

def leer_archivo_texto():
    
    print("\n--- LECTURA DE ARCHIVOS DE VENTAS ---")

    archivo_nombre = input("Ingrese el nombre del archivo .txt a leer (ej. ventas_12_06_2026.txt): ")

    try:
        with open(archivo_nombre, "r") as archivo:
            print(f"\n--- Contenido de {archivo_nombre} ---")
            print(archivo.read())
            print("---------------------------------------")

    except FileNotFoundError:
        print(f"El archivo '{archivo_nombre}' no existe.")

usuario = gestionar_usuarios()
    
print(f"\nHola, {usuario}")

pantalla_carga()

fecha_actual = capturar_fecha()
    
menu_matriz = [
    [1, "Iniciar Módulo de Pedidos"],
    [2, "Leer Archivo de Ventas (.txt)"],
    [3, "Cambiar Fecha de Operación"],
    [4, "Salir"]
]
    
activo = True

while activo:
    print("="*40)
    print("           MENÚ PRINCIPAL           ")
    print("="*40)
    for fila in menu_matriz:
        print(f"[{fila[0]}] {fila[1]}")
    print("="*40)
        
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Ingrese un número válido.")
        continue
            
    if opcion == 1:
        taqueria_pedidos(fecha_actual)
    elif opcion == 2:
        leer_archivo_texto()
    elif opcion == 3:
        fecha_actual = capturar_fecha()
    elif opcion == 4:
        print(f"Hasta luego, {usuario}")
        activo = False
    else:
        print("Opción fuera de rango.")
