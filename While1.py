'''
    Ejemplo Sintaxis.
    Tenemos una lista de n elementos
    y queremos que vaya eliminando cada
    elemento hasta que quede vacía lo
    realizaremos utilizando while
    y lo haremos con la función pop.
'''
# Tenemos está lista que contiene 5 elementos
z = ["Cuaderno","Lapicero","Laptop","Mouse","Teclado"]
# Mientras z esté definida
while z:
    # Se eliminará elemento por elemento.
    # Hasta que quede vacía.
    z.pop(0)
    # Mostramos la lista final.
    print(z)