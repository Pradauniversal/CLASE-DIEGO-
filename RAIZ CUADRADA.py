# Calcular la raíz cuadrada de un número y escribir su resultado. 
# Considerando el caso en que el número sea negativo

# El módulo cmath Este modulo proporciona acceso a funciones matemáticas para números complejos. 
# Las funciones de este módulo aceptan números enteros, números de coma flotante o números complejos como argumentos. 
# Aceptarán además cualquier objeto de Python que tenga tanto un método __complex__() o un método __float__() : 
# estos métodos son usados para convertir el objeto a un número complejo o de coma flotante, respectivamente, 
# y la función es entonces aplicada al resultado de la conversión.
#  también nos permite usar funciones matemáticas regulares con números complejos. 
# Por ejemplo, puede calcular la raíz cuadrada de un número complejo usando sqrt(z)

import cmath

numero = float(input("Ingrese un número: "))

raiz_cuadrada = cmath.sqrt(numero)

print("La raíz cuadrada de", numero, "es:", raiz_cuadrada)



