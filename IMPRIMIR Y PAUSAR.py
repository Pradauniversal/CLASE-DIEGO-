# Realiza un programa que imprima una secuencia de numeros de uno en uno desde el
# que el usuario desee, el programa debe pedirle al usuario después de que imprima un
# numero en pantalla le pregunte si desea continuar o no mostrando en pantalla


while True:
    inicio = int(input("Ingresa el número de inicio de la secuencia: "))
    
    # Imprimir la secuencia de números
    numero = inicio
    while True:
        numero += 1
        print(numero)
        
        opcion = input("¿Deseas continuar? (si/no): ")
        if opcion.lower() != 'si':
            break
