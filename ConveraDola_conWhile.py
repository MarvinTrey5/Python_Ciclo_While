#Variables del enunciado

#menu = ""
#lemp = 0.041
#cordo = 0.028
#quet = 0.13
men = "si"
print("1. Lempiras")
print("2. Córdovas")
print("3. Quetzales")
#proceso
#Iniciaremos convertiendo Lempiras a dólares
while men == "si":
    #print(menu)
    op = int(input("Elija una opción: "))
    if op == 1:
        lemp = float(input("Ingrese el valor de lempiras: "))
        dolar = lemp * 0.41
        print("El total en dólares es: $ ",dolar)
    elif op == 2:
        cordo = int(input("Ingrese el valor de córdova: "))
        dolar = cordo * 0.028
        print("El total en dólares es: $ ",dolar)
    elif op == 3:
        quet = int(input("Ingrese el valor de quetzales: "))
        dolar = quet * 0.13
        print("El total en dólares es: $ ",dolar)
    men = input("¿Desea hacer otra conversión? si o no: ")
    print(men)
    print("Fin del programa")
    