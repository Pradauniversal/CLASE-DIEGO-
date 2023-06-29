

nom_trab = input("agregar nombre: ")
num_h = int(input("agregar numero de horas: "))
tarifa_h = float(input("ingresar tarifa por hora: "))
salario_neto =""
impuestos=""
cant_h_extr = num_h - 140
tar_h_extr = tarifa_h * 1.5
tar_tot_h_etr = cant_h_extr * tar_h_extr
salario_mensual = 140 * tarifa_h + tar_tot_h_etr
salario_base =num_h * tarifa_h
salario_semanal = salario_base / 4
if tarifa_h > 14.28:
      salario_neto= salario_base
      

if salario_base > 2000 and salario_base < 2220:
      salario_neto = salario_base - salario_base *20 /100
elif salario_base > 2220:
      salario_neto = salario_base - salario_base *30 / 100
else:
     salario_neto = salario_base



if salario_base > 2000 and salario_base < 2220:
      impuestos =  salario_base *20 /100
elif salario_base > 2220:
      impuestos =  salario_base *30 / 100
else:
     impuestos = salario_base
print("su salario neto es: ", salario_base)
print("su salario semanal: ",salario_semanal)
print("sus impuestos son: ",impuestos)
print(f"{nom_trab} su salario mensual menos impuestos es igual a : {salario_neto}")