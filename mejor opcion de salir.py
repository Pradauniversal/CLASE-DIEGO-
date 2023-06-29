# Tatiana tiene ganas de salir con su amiga Paola a tomar un cafe pero ella sabe que si va 
# al centro comercial Campanario deberá pagar transporte ida y regreso y los cafes de ambas, 
# pero si va a Terraplaza se ahorra el transporte , 
# pero tambien debe tener encuenta que el cafe en Terraplaza 
# es 2 veces mas costoso que en campanario el cual tiene un costo de 4000 y tambien cuenta con 20000 
# el tranporte seria en bus por un valor de 1600 
# el programa le debe decir  a Tatiana cual seria la mejor opcion que debe tomar
presupuesto=20000
costo_cafe_campanario = 4000
costo_transporte_bus = 1600
costo_transporte_campanario = costo_transporte_bus *4
costo_cafe_terraplaza = costo_cafe_campanario * 2

gasto_campanario = costo_transporte_campanario + costo_cafe_campanario *2
gasto_terraplaza = costo_cafe_terraplaza *2
opcion_campanario = presupuesto - costo_cafe_campanario * 2 + costo_transporte_campanario 
opcion_terraplaza = presupuesto - costo_cafe_terraplaza * 2

if opcion_campanario < opcion_terraplaza:
    print("La mejor opción para Tatiana es ir al centro comercial Campanario.")
    print("ahorro total: ", opcion_campanario)
    print("gasto total: ",gasto_campanario)
else:
    print("La mejor opción para Tatiana es ir a Terraplaza.")
    print("ahorro total: ", opcion_terraplaza)
    print("gasto total: ",gasto_terraplaza)
