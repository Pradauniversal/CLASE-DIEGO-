# Realiza un programa que muestre los numeros impares desde un numero
# predeterminado hasta otro numero predeterminado


inicio = int(input("Ingrese el numero inicial: "))
final = int(input("Ingrese el numero final: "))

if inicio % 2 == 0:
    inicio += 1

print("los numeros impares entre ", inicio, "y ", final, " son: ")
for num in range(inicio, final + 1, 2):
    print(num)
