import pdb

boleto_bbt=0
boleto_adot=0
boleto_adultost=0

t_bb=0
t_ado=0
t_adul=0

d_ado=0
d_prof=0
d_may=0
d_stu_adul=0

print("**Precios base de entrada:**\n| Tipo de visitante | Precio |\n| :--- | :---: |\n| Niños menores de 3 años | Gratis ($0) |\n| Menores de edad (de 3 a 17 años) | $30 |\n| Mayores de 18 años | $45 |\n")
print("\n**Tabla de descuentos oficial:**\n| Tipo de visitante | Descuento |\n| :--- | :---: |\n| Adulto mayor | 12% |\n| Profesor | 10% |\n| Estudiante | 10% |\n")
np = int(input("Cuantas personas son? "))


for i in range(1, np+1):

    edad = int(input(f"Ingresa la edad de la persona {i}: "))

    if(edad < 3):
        boleto_bb = 0
        boleto_bbt += 1
    elif(edad <= 17):
        boleto_adot += 1
        t_ado +=30
        des_stu = input("Es estudiante? ")
        if(des_stu == "si"):
            d_ado += 3
    elif(edad <= 59):
        boleto_adultost += 1
        t_adul +=45
        print("\n**Tabla de descuentos oficial:**\n| Tipo de visitante | Descuento |\n| :--- | :---: |\n| Profesor | 10% |\n| Estudiante | 10% |\n")
        decision = int(input("Solo puedes elegir un descuento cual sera?\n1.Profesor\n2.Estudiante\n"))
        if(decision == 1):
            d_prof += 4.5
        elif(decision == 2):
            d_stu_adul += 4.5
    else:
        boleto_adultost += 1
        t_adul +=45
        d_may += 5.4


tt_adul = ((t_adul-d_prof)-(d_may))-(d_stu_adul)

print(f"Boletos de bebe totales: {boleto_bbt}")
print(f"Pago total de bebe totales: {t_bb}")
print(f"Boletos de menores totales: {boleto_adot}")
print(f"Pago total de menores totales: {t_ado-d_ado:.2f}")
print(f"Boletos de adultos totales: {boleto_adultost}")
print(f"Pago total de adultos totales: {tt_adul:.2f}")
