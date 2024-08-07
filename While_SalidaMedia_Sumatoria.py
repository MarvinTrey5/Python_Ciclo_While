# Hacer un ejercicio en Python que mediante 
# un ciclo while presente la
# salida de los números de 1 al 10
#  y muestre el cálculo de la media y la
# sumatoria de todos los números.

print("Se presentan los números del enunciado.")
print("--------------------------------")
suma=0
i=1
while i<=10:
      print(i," ",end="")
      suma=suma+i
      i+=1
print("")
print("---------------------------------")
print("La Sumatoria de los números es: ",suma)
print("El cálculo de la media es: ",suma/10) 

print("Fin del ejercicio")