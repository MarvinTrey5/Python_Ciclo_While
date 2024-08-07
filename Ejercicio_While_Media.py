# Pedir al usuario que ingrese una lista de números positivos, hacer lo siguiente:
# Sacar la cuenta de todos los números ingresados.
# Sacar la media de todos los números ingresados.
# Hacer un conteo de todos los números que se repiten

#Hecho por Marvin Fernández A1-Ténico

print("-----------------------")
print("SUMA Y MEDIA DE NUMEROS")
print("-----------------------")
numeros = int(input("Escriba un número( 0 o negativo termina): ")) # Ingresa los números
suma = 0 # inicia en 0
cuenta = 0 # inicia en 0
while numeros > 0: # mientras la variable del numeros ingresados sea mayor a 0
    cuenta += 1 # cuenta que esta en 0 recibe un aumento de + 1
    suma += numeros # suma que esta en 0, recibe el aumento de los números que ingreso
    numeros = int(input("Escriba otro numero(0 o negativo termina): ")) # si es mayor a 0 nos seguirá preguntando
print("")
print("----------------------")
print(f"Estos números se han ingresado: {cuenta} números") # cuenta almacena el total de números positivos que ingresamos
print(f'La Suma de los números ingresados es: {suma}') # suma almacena la suma de todos los númeos positivos
print(f'La Media de los números ingresados es: {suma/cuenta}') # suma/cuenta es el total de la suma y se divide entre la cuenta.

print("Fin del ejercicio")