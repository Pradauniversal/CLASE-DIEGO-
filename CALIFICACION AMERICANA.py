# El sistema de calificación americano (de Estados Unidos) se suele calcular de
# acuerdo al siguiente cuadro: (Utilizando esta información, escribir un algoritmo que
# acepte una calificación numérica del estudiante (0-100), convierta esta calificación a
# su equivalente en letra y visualice la calificación correspondiente en letra)
# Grado numérico Grado en letra
# Grado mayor o igual a 90    A
# Menor de 90 pero mayor o igual a 80  B
# Menor de 80 pero mayor o igual a 70  C
# Menor de 70 pero mayor o igual a 69  D
# Menor de 69        F

estudiante= input("ingresar nombre del estudiante: ")
calificacion = float(input("Ingrese la calificación numérica del estudiante de 0 a 100: "))

if calificacion >= 90:
    letra_de_calificacion = "A"
elif calificacion >= 80:
    letra_de_calificacion = "B"
elif calificacion >= 70:
    letra_de_calificacion = "C"
elif calificacion >= 60:
    letra_de_calificacion = "D"
else:
    letra_de_calificacion = "F"

print("la calificación numerica del estudiante", estudiante, " es: ", calificacion)
print("La calificación americana del estudiante", estudiante, " es:", letra_de_calificacion)
