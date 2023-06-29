# Escribir un programa que contenga una contraseña inventada, que le pregunte al
# usuario la contraseña, y no le permita continuar hasta que la haya ingresado
# correctamente.


usuario= input("ingresar usuario: ")
contraseña = "123467890"  
while True:
    ingresar_contraseña = input("Ingrese la contraseña: ")

    if ingresar_contraseña == contraseña:
        print(usuario)
        print("¡Bienvenido!")
        break
    else:
        print("Contraseña incorrecta. Inténtelo nuevamente.")


#------

usuario= input("ingresar usuario: ")
contraseña = "1234567890"  
intentos = 3

while intentos > 0:
    ingresar_contraseña = input("Ingrese la contraseña: ")

    if ingresar_contraseña == contraseña:
        print(usuario)
        print("¡Bienvenido!")
        break
    else:
        intentos -= 1
        print("Contraseña incorrecta. Le quedan", intentos, "intentos.")

if intentos == 0:
    print("Acceso denegado.")

#------


import time

usuario= input("ingresar usuario: ")
contraseña = "1234567890"  
intentos = 3
pausa_inicial = 3 

while intentos > 0:
    ingresar_contraseña = input("Ingrese la contraseña: ")

    if ingresar_contraseña == contraseña:
        print(usuario)
        print("¡Bienvenido!")
        break
    else:
        intentos -= 1
        print("Contraseña incorrecta. Le quedan", intentos, "intentos.")

        if intentos > 0:
            duracion_pausa = pausa_inicial * (intentos + 1)
            print("Esperando", duracion_pausa, "segundos...")
            time.sleep(duracion_pausa)

if intentos == 0:
    print("Se han agotado todos los intentos. Acceso denegado.")

#------
import time
usuario= input("ingresar usuario: ")


def verificar_contraseña():
    contraseña = "1234567890" 
    intentos = 3
    pausa_inicial = 3

    while intentos > 0:
        ingresar_contraseña = input("Ingrese la contraseña: ")

        if ingresar_contraseña == contraseña:
            print(usuario)
            print("¡Bienvenido!")
            return True
        else:
            intentos -= 1
            print("Contraseña incorrecta. Le quedan", intentos, "intentos.")

            if intentos > 0:
                duracion_pausa = pausa_inicial * (intentos + 1)
                print("Esperando", duracion_pausa, "segundos...")
                time.sleep(duracion_pausa)

    print("Se han agotado todos los intentos. Acceso denegado.")
    return False

if verificar_contraseña():
    print("Continuación del programa...")
else:
    print("No se pudo verificar la contraseña. Fin del programa.")
