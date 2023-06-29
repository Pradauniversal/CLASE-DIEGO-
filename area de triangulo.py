#crear un programa que permta determinar el area de un triangulo

def calcular_area_del_triangulo(base, altura):
    area = (base * altura) / 2
    return area

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

area_triangulo = calcular_area_del_triangulo(base, altura)

print("El área del triángulo es:", area_triangulo)