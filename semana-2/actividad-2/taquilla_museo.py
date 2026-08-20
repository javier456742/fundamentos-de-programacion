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
    else:
        boleto_adultost += 1
        t_adul +=45
        des_prof = input("Eres profesor? ")
        des_may = input("Es un adulto mayot? ")

        if(des_prof == "si" and des_may == "si"):
            d_prof += 4.5
            d_may += 5.4
        elif(des_prof == "si" and des_may == "no"):
            d_prof += 4.5
        elif(des_prof == "no" and des_may == "si"):
            d_may += 5.4

tt_adul = (t_adul-d_prof)-(d_may)

print(f"Boletos de bebe totales: {boleto_bbt}")
print(f"Pago total de bebe totales: {t_bb}")
print(f"Boletos de adolescentes totales: {boleto_adot}")
print(f"Pago total de adolescentes totales: {t_ado-d_ado}")
print(f"Boletos de adultos totales: {boleto_adultost}")
print(f"Pago total de adultos totales: {tt_adul}")
