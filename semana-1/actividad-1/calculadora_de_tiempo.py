#actividad 1 calculadora
name = input("Hola, Cual es tu nombre?")
act1 = float(input("Cuantas horas dedicas a redes sociales?"))
act2 = float(input("Cuantas horas dedicas a video juegos?"))
act3 = float(input("Cuantas horas dedicas a aplicaciones de entretenimiento/streaming(netflix o similares)?"))
act4 = float(input("Cuantas horas dedicas a tareas en el telefono?"))
act5 = float(input("Cuantas horas dedicas a otra actividad que no entre en las anteriores?"))

horas_totales = (act1+act2+act3+act4+act5)
porcentaje = (horas_totales*100)/(24)

print(f"{name}, tus horas totales gastadas en plataformas es {horas_totales} de 24 horas que tiene el dia.\n El porcentaje de tiempo es {porcentaje}% del 100% de las 24 horas del dia.")