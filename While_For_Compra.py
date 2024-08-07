def Lista_Compras(*comprados):
    i=0
    """ for comprado in comprados:
        print(f"{i}-{comprado}")
        i+=1 """
    """ for posicion, lista in enumerate(listaado):
        print(f"posición: {posicion + 1} producto: {lista}") """
    for comprado in comprados[0]:
        print(f"{i+1} - {comprado}")
        i+=1
listaado = []
while True:
    compra = input("Que es lo que desea comprar: ")
    listaado.append(compra)
    opc = input("Vas a comprar algo s/n: ")
    if(opc == "n"):
        Lista_Compras(listaado)
        break