#que el ususario ingrese una serie de numeros y al mismo tiempo
#ir sumando, el programa termina cuando
#el usuario ingrese un -1
print("--------------------------------")
total = 0   #acumulador
num = 1     #variable de control para el while
while num != -1:  #si la condicion se cumple inicia el ciclo
    num = int(input("Ingrese un número: ")) #pide un numero para ser evaluado y sumado
    total += num #hace la suma y acumula
    #print(num)   # imprime unicamente el numero que se ingresa

print("La suma de los números es: ",total) # muestra al suma de los numeros
print("Fin del programa")                   # cierre del programa