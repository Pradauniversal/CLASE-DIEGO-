# Construye un programa que Si distancia es mayor que 20 y menos que 35, 
# lee un valor para tiempo y calcula la Velocidad si Distancia = Velocidad * Tiempo

distancia = float(input("Ingrese la distancia: "))

if distancia > 20 and distancia < 35:
    tiempo = float(input("Ingrese el tiempo: "))
    velocidad = distancia / tiempo
    print("La velocidad es:", velocidad)
else:
    print("La distancia no está en el rango válido.")

#----

distancia = float(input("Ingrese la distancia: "))

if distancia >= 20 and distancia <= 35:
    tiempo = float(input("Ingrese el tiempo: "))
    velocidad = distancia / tiempo
    print("La velocidad es:", velocidad)
else:
    print("La distancia no está en el rango válido.")

#-----
distancia = float(input("Ingrese la distancia: "))


tiempo = float(input("Ingrese el tiempo: "))
velocidad = distancia / tiempo
print("La velocidad es:", velocidad)
