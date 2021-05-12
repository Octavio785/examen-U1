#definicion de variables u otros
print("Ejercicios de examen")
bono=0
#Datos de Entrada
o=int(input("Puntos obtenidos:"))
a=int(input("Salario minimos:"))
#Proceso
if o<=100:
  bono=((10*a)/100)
elif o<=150:
  bono=((40*a)/100)
elif o>=151:
  bono=((70*a)/100)
#Datos de Salida
print("El bono es: ", bono)
print("O.A.R.C.")