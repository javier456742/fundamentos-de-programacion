def menu_tuplas():

    numeros = (10, 20, 30, 40, 50)

    print("Tercer elemento:", numeros[2])

    n_1 = float(input("Ingrese el primer numero adicional: "))
    n_2 = float(input("Ingrese el segundo numero adicional: "))

    nueva_tupla = numeros + (n_1, n_2)
    lista_ordenada = sorted(list(nueva_tupla))

    print("Tupla resultante:", nueva_tupla)
    print("Lista ordenada:", lista_ordenada)

    def sumar_tupla(tup):
        
        return sum(tup)
    total = sumar_tupla(nueva_tupla)

    print("Suma total de los elementos:", total)

def menu_diccionarios():

    contactos = {
        "Carlos": "555-1234",
        "Sofia": "555-5678",
        "Miguel": "555-9012"
    }

    nombre = input("Ingrese el nombre del nuevo contacto: ")
    telefono = input("Ingrese el telefono del nuevo contacto: ")
    contactos[nombre] = telefono

    print("Nombres de los contactos registrados:")

    for c in c.keys():
        print("-", c)

    def obtener_telefono(dicc, nom):
        return dicc.get(nom)
    
    buscar = input("Ingrese el nombre del contacto a buscar: ")
    result = obtener_telefono(c, buscar)

    if result:
        print(f"El telefono de {buscar} es: {result}")
    else:
        print(f"No se encontro el contacto {buscar}")

def menu_excepciones():

    try:

        n_t_1 = input("Ingrese el primer numero entero: ")
        n_t_2 = input("Ingrese el segundo numero entero: ")

        n1 = int(n_t_1)
        n2 = int(n_t_2)

        print("La suma es:", n1 + n2)
        div = n1 / n2
        print(f"La division de {n1} entre {n2} es: {div}")

    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero. Ingresa un divisor distinto de 0.")

    except ValueError:
        print("Error: Debes ingresar valores numéricos enteros válidos.")

def menu_strings():

    mensaje = "Python es un lenguaje poderoso"

    print("Longitud del mensaje:", len(mensaje))
    print("En mayusculas:", mensaje.upper())

    remplazo = input("Ingresa la palabra que servira de reemplazo: ")
    mensaje_reemplazado = mensaje.replace("Python", remplazo)

    print("Texto reemplazado:", mensaje_reemplazado)

    def contar_palabras(texto):

        return len(texto.split())

    cant = contar_palabras(mensaje)

    print("Cantidad de palabras en el mensaje original:", cant)

while True:
    print("\n=== MENU PRINCIPAL ===")
    print("1. Sección Tuplas")
    print("2. Sección Diccionarios")
    print("3. Sección Excepciones")
    print("4. Sección Strings")
    print("5. Finalizar")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        menu_tuplas()
    elif opcion == "2":
        menu_diccionarios()
    elif opcion == "3":
        menu_excepciones()
    elif opcion == "4":
        menu_strings()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")