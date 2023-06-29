# Escribir una aplicación que reciba un número entero ke imprima su falla en factores primos.

numero = int(input("Ingrese un número entero: "))
def descomposicion_factores_primos(numero):
    factor = 2
    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero //= factor
        else:
            factor += 1

print("La descomposición en factores primos de", numero, "es:")
descomposicion_factores_primos(numero)

