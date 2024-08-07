#Estructura de repetición while     # += es un incremento secuencial va sumando de 1 en 1.
# paso 1 : crear un contador
num =   0                        # num = 1 cuando inicia
# paso 2: la condición              # num += 1 estamos sumandole 1 , cuando vale num? 2 osea 1 + 1
rango = int(input("Ingresa el rango: "))
while num <= (rango):
    print(num, "")
   #  print(" , ")

    # paso 3:incremento del contador
    num = num + 1
print(num)


# El operador "=" es para asignar un valor a una varibale
# el operador "==" es para comparar.

#siga = "si"

#while siga == "si":
#    print("siguiendo")
#    siga = input("¿Continuar? si o no: ")

#print("Fin del programa")