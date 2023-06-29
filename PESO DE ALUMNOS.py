# Se desea realizar una estadística de los pesos de los alumnos de un colegio de
# acuerdo a la siguiente tabla:
# Alumnos de menos de 40 kg.
# Alumnos entre 40 y 50 kg.
# Alumnos de más de 50 kg y menos de 60 kg.
# Alumnos de más o igual a 60 kg.


alumnos_menos_40kg = 0
alumnos_40_50kg = 0
alumnos_50_60kg = 0
alumnos_mas_60kg = 0

cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

for i in range(cantidad_alumnos):
    peso = float(input(f"Ingrese el peso del alumno {i+1}: "))

    if peso < 40:
        alumnos_menos_40kg += 1
    elif peso >= 40 and peso < 50:
        alumnos_40_50kg += 1
    elif peso >= 50 and peso < 60:
        alumnos_50_60kg += 1
    else:
        alumnos_mas_60kg += 1

print("Estadísticas de pesos de los alumnos:")
print("Alumnos de menos de 40 kg:", alumnos_menos_40kg)
print("Alumnos entre 40 y 50 kg:", alumnos_40_50kg)
print("Alumnos de más de 50 kg y menos de 60 kg:", alumnos_50_60kg)
print("Alumnos de más o igual a 60 kg:", alumnos_mas_60kg)
