'''
    Ejemplo 4 while anidados.
    Generaremos una permutación
'''
# Tenemos estas 2 variable inicializadas en 0.
n = 0
m = 0
# Mientras n sea < a 3
while n <3:
    # Mientras m sea < a 3.
    while m < 3:
        # Mostramos los númeos que se van almacenando
        print(n,m)
        # La variable m se incrementará en 1
        m += 1
    # De igual manera la variable del primer while.
    n += 1
    # Hasta que llegue a 2 2
    m = 0