'''
    Ejemplo 3 while.
    Tenemos esté ejemplo base 
    donde utilizaremos el break.
'''
# Variable entera.
z = 6
# Creamos un while verdadero a
# ejecutarse
while True:
    # z que vale 6 tendrá un decremento -1.
    z -=1
    # Mostramos en pantalla.
    print(z)
    # Colocamos una condicion
    # si la variable z es igual (llega a 0)
    if z == 0:
        # break significa cortar el código
        break
# No hay necesidad de utilizar else o mensajes
else:
    print("Fin del bucle")