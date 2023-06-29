def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mcm(a, b):
    return (a * b) // mcd(a, b)

def fraccion_simple(numerador, denominador):
    divisor_comun = mcd(numerador, denominador)
    numerador_simplificado = numerador // divisor_comun
    denominador_simplificado = denominador // divisor_comun
    return numerador_simplificado, denominador_simplificado

def suma_de_fracciones(fraccion1, fraccion2, fraccion3):
    denominador = mcm(fraccion1[1], mcm(fraccion2[1], fraccion3[1]))
    numerador = fraccion1[0] * (denominador // fraccion1[1]) + fraccion2[0] * (denominador // fraccion2[1]) + fraccion3[0] * (denominador // fraccion3[1])
    return fraccion_simple(numerador, denominador)

num1 = int(input("Ingrese el numerador de la primera fracción: "))
den1 = int(input("Ingrese el denominador de la primera fracción: "))

num2 = int(input("Ingrese el numerador de la segunda fracción: "))
den2 = int(input("Ingrese el denominador de la segunda fracción: "))

num3 = int(input("Ingrese el numerador de la tercera fracción: "))
den3 = int(input("Ingrese el denominador de la tercera fracción: "))


fraccion1 = fraccion_simple(num1, den1)
fraccion2 = fraccion_simple(num2, den2)
fraccion3 = fraccion_simple(num3, den3)

result = suma_de_fracciones(fraccion1, fraccion2, fraccion3)

print("La suma de las fracciones es: {}/{}".format(result[0], result[1]))
