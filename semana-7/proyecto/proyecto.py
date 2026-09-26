import time

# Define el tiempo de espera para preguntar si seguir

TIEMPO_MAXIMO_INACTIVIDAD = 10 *  600 


def verificar_inactividad_con_for(ultima_actividad):

    # Si pasan 10 min sin haccer algo pregunta si continuar

    if time.time() - ultima_actividad < TIEMPO_MAXIMO_INACTIVIDAD:
        return ultima_actividad

    print("\nAlerta: Se han detectado 10 minutos de inactividad.")
    for intento in range(1, 4):
        respuesta = (
            input('¿Deseas continuar en la sesión? Escribe "si" o "no": ')
            .strip()
            .lower()
        )
        if respuesta == "si":
            print("Reanudando sesión...")
            return time.time()
        if respuesta == "no":
            print("Regresando al inicio de sesión...")
            return "reiniciar"
        print(
            f'Intento {intento}/3. Respuesta no válida. Debe escribir "sí" o "no".'
        )

    print("Demasiados intentos fallidos. Cerrando sesión.")
    return "reiniciar"

def pantalla_carga():
    
    # Muestra una animación simple de carga al iniciar el programa.
    
    print("\n[SISTEMA] Iniciando programa...")
    
    for segundo in range(1, 6):
        print(f"Cargando... {segundo}/5 segundos")
        time.sleep(1)
    print("Sistema cargado con éxito\n")

def gestionar_usuarios():
    
    # Gestiona el registro e inicio de sesión guardando usuarios y contraseñas en archivos separados

    archivo_usuarios = "usuarios.txt"
    archivo_contras = "contras.txt"
    
    try:
        with open(archivo_usuarios, "r") as f_u, open(archivo_contras, "r") as f_c:
            usuarios_registrados = f_u.read().splitlines()
            usuarios_contras = f_c.read().splitlines()
    except FileNotFoundError: 
        with open(archivo_usuarios, "w") as f_u, open(archivo_contras, "w") as f_c:
            usuarios_registrados = []
            usuarios_contras = []

    print("="*40)
    print(" ACCESO DE USUARIOS ")
    print("="*40)
    print("1. Iniciar sesion")
    print("2. Registrar nueva cuenta")

    opcion = input("Seleccione una opción (1 o 2): ")

    if opcion == "1":

        usuario = input("Ingrese su nombre de usuario: ")
        contra = input("Ingrese su contraseña de usuario: ")

        if usuario in usuarios_registrados:
            indice = usuarios_registrados.index(usuario)
            if usuarios_contras[indice] == contra:
                print(f"\nBienvenido de nuevo, {usuario}.")
                return usuario

        print("\nEl usuario no esta registrado o la contraseña es incorrecta. Intente de nuevo o registrese.")
        return gestionar_usuarios()
            
    elif opcion == "2":

        nuevo_usuario = input("Elija un nombre de usuario nuevo: ")
        nueva_contra = input("Elija una contraseña de usuario nueva: ")

        if nuevo_usuario in usuarios_registrados:
            print("\nEse usuario ya existe. Intente iniciar sesión.")
            return gestionar_usuarios()
        
        else:
            with open(archivo_usuarios, "a") as f_u, open(archivo_contras, "a") as f_c:
                f_u.write(nuevo_usuario + "\n")
                f_c.write(nueva_contra + "\n")
            print(f"\nCuenta creada y guardada con exito, bienvenido, {nuevo_usuario}.")
            return nuevo_usuario

    else:
        print("Opción invalida.")
        return gestionar_usuarios()

def capturar_fecha():
    
    # Captura y devuelve una tupla con la fecha de operación ingresada por el usuario.
    
    print("\n--- CAPTURA DE FECHA DE OPERACIÓN ---")
    
    dia = input("Ingrese el día (ej. 12): ")
    mes = input("Ingrese el mes (ej. 06): ")
    anio = input("Ingrese el año (ej. 2026): ")
    
    Fecha = (dia, mes, anio)
    
    print(f"Fecha registrada: {Fecha[0]}/{Fecha[1]}/{Fecha[2]}")
    
    return Fecha

def registrar_en_indice(nombre_archivo):
    
    #Registra el nombre del archivo en 'registro_ventas.txt' asignándole un número único si no existe ya.

    archivo_indice = "registro_ventas.txt"
    archivos_existentes = []
    
    # Leer el índice actual si existe
    
    try:
        with open(archivo_indice, "r") as f:
            archivos_existentes = f.read().splitlines()
    except FileNotFoundError:
        pass
        
    # Verificar si el archivo ya está registrado (para no duplicarlo)
    
    if nombre_archivo not in archivos_existentes:
        archivos_existentes.append(nombre_archivo)
        # Reescribir todo el índice con la numeración actualizada
        with open(archivo_indice, "w") as f:
            for i, nombre in enumerate(archivos_existentes, start=1):
                f.write(f"{i}-{nombre}\n")

def taqueria_pedidos(fecha_actual):
    
    # Controla el registro de pedidos por mesa y calcula el total de ventas del día.
    
    total_dia = 0
    num_pedidos = 0
    continuar_cliente = "si"
    
    while continuar_cliente.lower() == "si":
        print("===================================")
        print("   TAQUERÍA LAS BRASAS DE OAXACA   ")
        print("===================================")
        
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

            # Guarda el ticket de venta en un archivo de texto diario

            with open(nombre_archivo, "a") as archivo:
                archivo.write(f"Fecha: {fecha_actual[0]}/{fecha_actual[1]}/{fecha_actual[2]} | Mesa: {numero_mesa} | Total: ${total_pedido}\n")

            # Registra y enumera automáticamente el archivo creado

            registrar_en_indice(nombre_archivo)

            print(f"-> Venta guardada en '{nombre_archivo}'.")
            
        else:
            print("Pedido cancelado o sin ítems.")
            
        continuar_cliente = input("¿Desea atender a otra mesa? (si/no): ")
        
    print(f"\n--- CORTE DEL DÍA ---\nMesas atendidas: {num_pedidos} | Ventas totales: ${total_dia}")

def leer_archivo_texto():

    # Lee y muestra en consola el contenido de un archivo de ventas buscando por su número asignado.
    
    print("\n--- LECTURA DE ARCHIVOS DE VENTAS ---")
    archivo_indice = "registro_ventas.txt"

    try:
        with open(archivo_indice, "r") as f:
            lineas = f.read().splitlines()
    except FileNotFoundError:
        print("No hay registros de ventas guardados todavía.")
        return

    if not lineas:
        print("El archivo de registro está vacío.")
        return

    print("\nDías de ventas registrados:")
    for linea in lineas:
        print(linea) # Muestra ej: 1-ventas_24_09_26.txt

    try:
        num_seleccionado = int(input("\nIngrese el número asignado al día de venta que desea ver: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    # Buscar el archivo correspondiente al número ingresado

    archivo_a_buscar = None
    for linea in lineas:
        partes = linea.split("-", 1) # Separa el número del nombre del archivo
        if len(partes) == 2 and partes[0].strip() == str(num_seleccionado):
            archivo_a_buscar = partes[1].strip()
            break

    if archivo_a_buscar:
        try:
            with open(archivo_a_buscar, "r") as archivo:
                print(f"\n--- Contenido de {archivo_a_buscar} ---")
                print(archivo.read())
                print("---------------------------------------")
        except FileNotFoundError:
            print(f"El archivo '{archivo_a_buscar}' no se encuentra en el sistema.")
    else:
        print("Número asignado no válido.")

# Ejecución inicial

usuario = gestionar_usuarios()

print(f"\nHola, {usuario}")

pantalla_carga()

fecha_actual = capturar_fecha()
    
menu_matriz = [
    [1, "Iniciar Módulo de Pedidos"],
    [2, "Leer Archivo de Ventas (.txt)"],
    [3, "Salir"]
]
    
activo = True
ultima_actividad = time.time()

while activo:
    res = verificar_inactividad_con_for(ultima_actividad)
    if res == "reiniciar":
        usuario = gestionar_usuarios()
        ultima_actividad = time.time()
        continue
    else:
        ultima_actividad = res

    print("="*40)
    print(" MENÚ PRINCIPAL ")
    print("="*40)
    for fila in menu_matriz:
        print(f"[{fila[0]}] {fila[1]}")
    print("="*40)
        
    try:
        opcion = int(input("Seleccione una opción: "))
        ultima_actividad = time.time()
    except ValueError:
        print("Ingrese un número válido.")
        ultima_actividad = time.time()
        continue
            
    if opcion == 1:
        taqueria_pedidos(fecha_actual)
        ultima_actividad = time.time()
    elif opcion == 2:
        leer_archivo_texto()
        ultima_actividad = time.time()
    elif opcion == 3:
        print(f"Hasta luego, {usuario}")
        activo = False
    else:
        print("Opción fuera de rango.")
        