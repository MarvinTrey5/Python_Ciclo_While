print("******* BIENVENIDO A PYTHON ******* ")
siga = "si" # variable de cofirmación
ID = "Programador" # Contraseña secreta
while siga == "si": # Si la resupuesta es si depués de que nos pregunte volveremos a intentarlo
    usuario = input("Ingresu su usuario: ") # Ingresamos el usuario
    contraseña = input("Ingrese su contraseña: ") # Ingresamos la contraseña
    if ID == contraseña: # Si el ID y la contraseña son iguales pues
        print("Puedes avanzar") # Nos mostrará esto
    else:                                    # Si no nos dirá lo siguiente
        print("Contraseña inválida") # Si fallamos nos dirá esto
    siga = input("Desea volver a intentarlo: ") # si fallamos nos preguntará esto
    print(siga)                                                  # Se alamcena nuestra respuesta
print("Fin del programa")                              # Si escogemos no pues saldremos del bucle
