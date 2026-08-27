# Fundamentos de Programación — Avance de Proyecto

## 1. Análisis Organizacional
* **Empresa:** Taquería *Las Brasas de Oaxaca*.
**Área de Impacto Operativo:** Gestión de inventarios, registro de ventas en mostrador/mesas y eficiencia en el tiempo de atención.* 
**Necesidad:** Actualmente, el establecimiento registra los pedidos manualmente en notas de papel y realiza el cálculo de las ventas diarias utilizando una calculadora al finalizar la jornada. Esto genera: errores, poca eficiencia, problemas de rapidez, etc.

## 2. Definición del Problema
* **Problemática:** Falta de un sistema digital centralizado de consola que organice la captura de comandas por mesa, aplique reglas de cobro ajustadas al menú y genere reportes automáticos del corte de caja diario.
* **Reglas de Negocio:** 
* **Menú Base:** El establecimiento ofrece productos típicos de taquería (tacos, quesadillas, alambres, aguas frescas, refrescos, etc.). 
* **Ajuste por Pieza Individual (Recargo):** Cuando un cliente solicita únicamente 1 pieza de un producto cuyo precio promocional de menú requiere ordenar 2 o más piezas (ej. promociones 2x1 o paquetes de 3), se aplica un recargo automático de **+$10.00 MXN** al precio base unitario. 
* **Validación de Pedidos Cero:** No se permiten cuentas finales con valor igual o menor a `$0.00`. Toda cantidad ingresada debe ser mayor a 0.
* **Atención Continua:** El sistema debe operar en un bucle continuo atendiendo mesa por mesa hasta que el operador decida cerrar la jornada de trabajo.

## 3. Listado de Requerimientos Funcionales
**1.-** **Despliegue de Menú:** Mostrar dinámicamente el catálogo interactivo de productos con sus precios actualizados.

**2.-** **Captura por Mesa:** Solicitar el número de mesa e iterar la adición de platillos/bebidas y cantidades hasta que la mesa concluya su pedido.

**3.-** **Cálculo de Recargos:** Aplicar el ajuste de **+$10 MXN** cuando el pedido consista en 1 sola unidad de una orden múltiple (promocional). 

**4.-** **Acumulación e Informe Final** Sumar los subtotales de cada mesa, mostrar el ticket desglosado y emitir el resumen del total de mesas atendidas y venta global del día.

## 4. Clasificación de Datos
`numero_mesa` = `int` Número identificador de la mesa atendida. 

`precio` = `int` Precio base unitario del producto seleccionado. 

`cantidad` = `int` Cantidad de porciones/unidades solicitadas.

`es_unidad_promocional` = `bool` Bandera que indica si aplica el recargo de +$10 por unidad individual. 

`subtotal` = `float` Suma acumulada de los productos solicitados por una mesa. 

`total_dia` = `float` Acumulador global con el total de ventas acumuladas en la jornada.

`seguir` = `bool` / `str` Variable de control para mantener activo el flujo de atención. 

## 5. Operadores del Lenguaje
* **Operadores Matemáticos (`+`, `-`, `*`):** Utilizados para sumar el total, aplicar el recargo de +$10 a piezas individuales y multiplicar el precio.* 

* **Operadores Relacionales (`==`, `>`, `!=`, `<=`, `>=`):** Empleados para opciones de menú, asegurar que la cantidad sea positiva (`cantidad > 0`) e identificar decisiones.* 

* **Operadores Lógicos (`and`, `or`, `not`):** Necesarios en la construcción de condiciones, entradas e iteraciones.

## 6. Estructuras de Control
* **Estructuras de Decisión (`if`, `elif`, `else`):**  

* **Estructuras Iterativas (`while y for`):**  

## 7. Diseño Algorítmico (Pseudocódigo Adaptado PSeInt)

```text
Algoritmo LasBrasasDeOaxaca
    Definir total_dia, subtotal, total_pedido, precio, recargo Como Real
    Definir opcion, cantidad, num_pedidos, numero_mesa Como Entero
    Definir continuar_cliente, respuesta_promo Como Cadena
    
    total_dia = 0
    num_pedidos = 0
    continuar_cliente = "si"
    
    Mientras continuar_cliente = "si" O continuar_cliente = "Si" Hacer
        Escribir "===================================="
        Escribir "       TAQUERÍA LAS BRASAS DE OAXACA"
        Escribir "===================================="
        Escribir "Ingrese el número de mesa:"
        Leer numero_mesa
        
        subtotal = 0
        opcion = 0
        
        Mientras opcion <= 6 Hacer
            Escribir ""
            Escribir "--- MENÚ DE PLATILLOS ---"
            Escribir "1. Orden Tacos al Pastor (3 pcs) - $60"
            Escribir "2. Orden Quesadillas Oaxaqueñas (2 pcs) - $50"
            Escribir "3. Alambre Especial de la Casa - $110"
            Escribir "4. Agua Fresca (1 L) - $30"
            Escribir "5. Refresco (600 ml) - $25"
            Escribir "6. Finalizar pedido de la mesa"
            Escribir "Seleccione una opción (1-6):"
            Leer opcion
            
            Si opcion >= 1 Y opcion <= 5 Entonces
                Escribir "Ingrese la cantidad solicitada:"
                Leer cantidad
                
                Si cantidad > 0 Entonces
                    recargo = 0
                    
                    Segun opcion Hacer
                        1:
                            precio = 60
                            // Regla de negocio: 1 taco suelto de orden de 3
                            Si cantidad = 1 Entonces
                                Escribir "¿El cliente desea solo 1 pieza individual en lugar de la orden completa? (s/n):"
                                Leer respuesta_promo
                                Si respuesta_promo = "s" O respuesta_promo = "S" Entonces
                                    precio = 25 // Precio base individual + $10 recargo
                                    recargo = 10
                                FinSi
                            FinSi
                        2:
                            precio = 50
                            // Regla de negocio: 1 quesadilla suelta de orden de 2
                            Si cantidad = 1 Entonces
                                Escribir "¿El cliente desea solo 1 pieza individual en lugar de la orden completa? (s/n):"
                                Leer respuesta_promo
                                Si respuesta_promo = "s" O respuesta_promo = "S" Entonces
                                    precio = 35 // Precio base individual + $10 recargo
                                    recargo = 10
                                FinSi
                            FinSi
                        3: precio = 110
                        4: precio = 30
                        5: precio = 25
                    FinSegun
                    
                    subtotal = subtotal + (precio * cantidad)
                    Si recargo > 0 Entonces
                        Escribir "-> Se aplicó un recargo de $10.00 MXN por pedido individual."
                    FinSi
                    Escribir "-> Ítem agregado. Subtotal mesa: $", subtotal
                Sino
                    Escribir "¡ERROR! La cantidad debe ser mayor a 0."
                FinSi
            Sino
                Si opcion > 6 Entonces
                    Escribir "¡ERROR! Opción inválida."
                FinSi
            FinSi
        FinMientras
        
        Si subtotal > 0 Entonces
            total_pedido = subtotal
            total_dia = total_dia + total_pedido
            num_pedidos = num_pedidos + 1
            
            Escribir ""
            Escribir "===================================="
            Escribir "RESUMEN DE CUENTA - MESA #", numero_mesa
            Escribir "Total a Pagar: $", total_pedido
            Escribir "===================================="
        Sino
            Escribir "Pedido cancelado o sin ítems registrados."
        FinSi
        
        Escribir "¿Desea atender a otra mesa? (s/n):"
        Leer continuar_cliente
    FinMientras
    
    Escribir ""
    Escribir "===================================="
    Escribir "    CORTE DE CAJA / RESUMEN DEL DÍA"
    Escribir "===================================="
    Escribir "Total de mesas atendidas: ", num_pedidos
    Escribir "Ventas totales de la jornada: $", total_dia
    Escribir "===================================="
FinAlgoritmo