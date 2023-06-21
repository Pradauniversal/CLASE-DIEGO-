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

# Leer los numeradores y denominadores de las fracciones
num1 = int(input("Ingrese el numerador de la primera fracción: "))
den1 = int(input("Ingrese el denominador de la primera fracción: "))

num2 = int(input("Ingrese el numerador de la segunda fracción: "))
den2 = int(input("Ingrese el denominador de la segunda fracción: "))

num3 = int(input("Ingrese el numerador de la tercera fracción: "))
den3 = int(input("Ingrese el denominador de la tercera fracción: "))

# Simplificar las fracciones
fraccion1 = fraccion_simple(num1, den1)
fraccion2 = fraccion_simple(num2, den2)
fraccion3 = fraccion_simple(num3, den3)

# Sumar las fracciones
result = suma_de_fracciones(fraccion1, fraccion2, fraccion3)

# Imprimir el resultado
print("La suma de las fracciones es: {}/{}".format(result[0], result[1]))


















# # Función para sumar tres fracciones
# num1 = int(input("ingresar num1: "))
# den1 = int(input("ingresar den1: "))
# num2 = int(input("ingresar den2: "))
# den2 = int(input("ingresar den2: "))
# num3 = int(input("ingresar num3: "))
# den3 = int(input("ingresar den3: "))

# def mcm (mcm= den1 * den2):
#     return mcm

# num1 = num1 * den2
# num2 = num2 * den1

# def suma_numeradores(num1, num2):
#     return suma_numeradores 


# num_suma2 = suma_numeradores, num3
# den_suma2 = mcm, den3
# int(num_suma2,"/", den_suma2:)
   


# def num_suma2(num1, num2, num3):
# def den_suma2(den1, den2, den3):

    # return num_suma2,den_suma2











# # algoritmo que sume fraccionarios

# num1 = int(input("ingresar num1"))
# den1 = int(input("ingresar den1"))
# num2 = int(input("ingresar den2"))
# den2 = int(input("ingresar den2"))
# num3 = int(input("ingresar num3"))
# den3 = int(input("ingresar den3"))
# def sumarFracciones(num1, den1, num2, den2, num3, den3):
# #Calcular el denominador común multiplicando los denominadores
# denominadorComun= den1 * den2 * den3


# num1 = num1 * (den2 * den3)
# num2 = num2 * (den1 * den3)
# num3 = num3 * (den1 * den2)
# #Sumar los numeradores
# sumaNumeradores=num1 + num2 + num3

# #Devolver la fracción resultante sin simplificar
#     return (sumaNumeradores, denominadorComun)


# resultadoNum, resultadoDen = sumarFracciones(num1, den1, num2, den2)

# print ("El resultado de la suma es:", resultadoNum, "/", resultadoDen)
