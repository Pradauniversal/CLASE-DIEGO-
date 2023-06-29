# Realizar  un programa para saber que día tiene pico y placa su vehículo


5


p = input("ingresar placa: ")

if len(p) == 6:
   

   try:
      x = int(p[5])
      vehiculo= " carro tiene "
   except:
      x = int(p[4])
      vehiculo = " moto tiene "
      
   if x == 1 or x == 2:
      print("su " + vehiculo +"tiene pico y placa el viernes")
   elif x == 3 or x == 4:
      print("su" + vehiculo + "tiene pico y placa el lunes")
   elif x == 5 or x == 6:
      print("su" + vehiculo + "tiene pico y placa el martes")
   elif x == 7 or x == 8:
      print("su" + vehiculo + "tiene pico y placa el miercoles")
   elif x == 0 or x == 9:
      print("su" +vehiculo + "tiene pico y placa eljueves")
      
   else:
      print("no tiene dia asignado")
else:
   print("placa imvalida")


#---if anidado

p = input("ingresar placa: ")

if len(p) == 6:
   

   try:
      x = int(p[5])
      vehiculo= " carro tiene"
   except:
      x = int(p[4])
      vehiculo = " moto tiene"
   if x == 1 or x == 2:
      print("su " + vehiculo + " pico y placa es el viernes")
   else:
      if x == 3 or x == 4:
         print("su " + vehiculo + " pico y placa es el lunes")
      else:
         if x == 5 or x == 6:
            print("su " + vehiculo + " pico y placa es el martes")
         else:
            if x == 7 or x == 8:
               print("su " + vehiculo + " pico y placa es el miercoles")
            else:
               if x == 0 or x == 9:
                  print("su " + vehiculo + " pico y placa es el jueves")
      
               else:
                 print("no tiene dia asignado")
else:
   print("placa imvalida")