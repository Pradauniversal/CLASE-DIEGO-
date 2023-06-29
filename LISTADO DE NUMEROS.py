# Elabora un programa que muestre una lista de números la cual pida al usuario desde
# que numero quiere y hasta que numero quiere mostrar por ejemplo si  ingresa  2  y 10
# debería mostrar  2,3,4,5,6,7,8,9,10 o si  ingresa  2  y -10  debería mostrar
# 2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10

inicio = int(input("Ingrese el número inicial: "))
fin = int(input("Ingrese el número final: "))

print("la lista de numeros es : ")  

if inicio <= fin:
    for numero in range(inicio, fin+1):
        print(numero, end=", ")
else:
    for numero in range(inicio, fin-1, -1):
        print(numero, end=", ")


