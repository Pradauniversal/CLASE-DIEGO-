numero = float(input("Ingrese un número: "))

if isinstance(numero, int):
    print("El número es entero.")
elif isinstance(numero, float):
    print("El número es real.")
else:
    print("El número no es válido.")


#----------

año = int(input("Ingrese un año: "))

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print(año, "es un año bisiesto.")
        else:
            print(año, "no es un año bisiesto.")
    else:
        print(año, "es un año bisiesto.")
else:
    print(año, "no es un año bisiesto.")
