# IMC WHILE

print("********** BIENVENIDO AQUI CALCULAREMOS TU IMC ***********")
print("********** DATOS PERSONALES ***********")
siga = "si"
Estado = ""
while siga == "si":
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    peso = int(input("Ingresa tu peso en Kg: "))
    altura = float(input("Ingresa tu estatura en Mts: "))
    IMC = peso / (altura * altura)
    if IMC < 50:
        Estado = "Delgadez"
    elif IMC >= 55:
        Estado = "Ideal"
    elif IMC >= 65:
        Estado = "Sobrepeso"
    elif IMC >= 70:
        Estado = "Obesidad Mórbida"
    siga = input("Desear calcular otro IMC: ")
    print(siga)
    print("*********** RESULTADOS OBTENIDOS ************")
    print("Tu nombre es: " + nombre)
    print("Tu Edad es: " + edad)
    print("Tu IMC es: " + str(IMC))
    print("Tu estado es: ", Estado)