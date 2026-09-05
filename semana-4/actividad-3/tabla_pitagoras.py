tabla = []

for i in range(1, 11):
    fila = []
    for j in range(1, 11):
        producto = 0
        for k in range(j):
            producto += i
        fila.append(producto)
    tabla.append(fila)

def mostrar_tabla(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()

def obtener_multiplicacion(matriz, factor1, factor2):
    return matriz[factor1 - 1][factor2 - 1]

mostrar_tabla(tabla)

print("\nConsulta de Multiplicación")

f1 = int(input("Ingresa el primer factor del 1 al 10: "))
f2 = int(input("Ingresa el segundo factor del 1 al 10: "))

resultado = obtener_multiplicacion(tabla, f1, f2)

print(f"El resultado de {f1} x {f2} es: {resultado}")