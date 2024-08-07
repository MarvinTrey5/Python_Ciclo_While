'''
    Ejemplo 5 while 3 anidados.
    Generaremos una permutación
'''
# Crearemos 2 variables con inicializador 0.
n,m,o = 0,0,0
# Las mismas condiciones que el anterior.
while n < 3:
    while m < 3:
        while o < 3:
            # Mostramos los elementos
            print(n,m,o)
            # cuando se ejecute el 3 while
            # tanto o y m van a recibir un 
            # incremento de + 1.
            o += 1
            m += 1
        # Fuera del tercer while (o) va a
        # hacer igual a 0.
        o = 0
    # Fuera del 3 y 2 while la variable n
    # va a recibir un incremento de + 1.
    n += 1
    # y el 2 while será igual a 0.
    m = 0