# Crea un Algoritmo que nos calcule el área de un triángulo conociendo sus lados
# s (semiperimetro) 

a=int(input("ingresar lado a: "))
b=int(input("ingresar lado b: "))
c=int(input("ingresar lado c: "))

import math

def calcular_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area


area_triangulo = calcular_area(a, b,c)
print("El área del triángulo es:", area_triangulo)
