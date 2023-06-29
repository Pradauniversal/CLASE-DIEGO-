#Elabora un programa para una discoteca que necesita controlar el acceso a las personas 
# la cual pida el nombre a una persona y su edad, en caso que sea mayor de 18 lo deje ingresar, 
# si es menor de edad debe mostrar un mensaje diciendole que no puede ingresar 
# y si tiene 18 años debe preguntar por su identificación

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Bienvenido(a),", nombre + "! Puedes ingresar a la discoteca.")
elif edad < 18:
    print("Lo siento,", nombre + ", no se permite el ingreso de menores.")
else:
    identificacion = input("Tienes 18 años. muestra tu identificación (Sí/No): ")
    if identificacion == "si":
        print("Bienvenido(a),", nombre + "! Puedes ingresar a la discoteca.")
    else:
        print("Lo siento,", nombre + ", sin identificación no puedes ingresar a la discoteca.")



