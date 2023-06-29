# Un ángulo se considera agudo si es menor de 90 grados, obtuso si es mayor de 90
# grados y recto si es igual a 90 grados. Utilizando esta información, escribir un
# algoritmo que acepte un ángulo en grados y visualice el tipo de ángulo
# correspondiente a los grados introducidos

angulo = float(input("Ingrese el valor del ángulo en grados: "))

if angulo < 90:
    tipo_angulo = "Agudo"
elif angulo > 90:
    tipo_angulo = "Obtuso"
else:
    tipo_angulo = "Recto"

print("El ángulo de",angulo, "grados es:", tipo_angulo)
