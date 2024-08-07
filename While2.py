'''
    Ejemplo 2 while.
    En python podemos utilizar el else del if.
    Tenemos esté ejemplo base
'''
# Tenemos una variable que inicia en 6
z = 6
# Si z es mayor a 0.
while z > 0:
    # Si se cumple realizará un decremento
    # es decir 5,4,3,2,1,0
    z -= 1
    # Mostramos la lista en decremento
    print(z)
# El else se ejecutará cuando termine el bucle 
# while.
else:
    # Mostrará el siguiente mensaje.
    print("Salió del bucle")