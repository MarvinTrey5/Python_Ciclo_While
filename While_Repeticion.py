# Bucles While :)
# Sirve como para hacer una repetición mientras se 
# cumpla una condición para ir pasando cliente por cliente
# para hacerle una modificación.

# creamos una varialble
contador = 0
while contador < 5:
    # Para que aumente 1 desde 0
    contador += 1
    # Para saltar un número es
    if contador == 3:
        continue
    print('El valor del contador es: ' + str(contador))