#Elabora un programa que Dados tres números de cuál es el central

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num2 < num1 < num3 or num3 < num1 < num2:
    numero_central = num1

elif num1 < num2 < num3 or num3 < num2 < num1:
    numero_central = num2

else:
    numero_central = num3

print("El número central es:", numero_central)
