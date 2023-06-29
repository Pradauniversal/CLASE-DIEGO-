# Calcular el factorial de un numero ingresado  por teclado, si el  factorial de un numero
# se  representa de la siguiente forma n! = 1*2*3*4*5......(n-1)*n    Ejemplo 2: 4! =
# 1*2*3*4  = 24; tenga en cuenta que el  factorial de 0! es 1   0! = 1


numero = int(input("Ingrese un número: "))

if numero == 0:
    factorial = 1
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i

print(f"El factorial de {numero} es: {factorial}")

