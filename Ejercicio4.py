#definicion de variables u otros
print("Ejercicios de examen")
resultado=0
#Datos de Entrada
o=int(input("Valor 1:"))
a=int(input("Valor 2:"))
s=int(input("Signo 1=+, 2=-, 3=*, 4=/ y 5=^:"))
#Proceso
if s==1:
  resultado=o+a
elif s==2:
  resultado=o-a
elif s==3:
  resultado=o*a
elif s==4:
  resultado=o/a
elif s==5:
  resultado=o**a
#Datos de Salida
print("El bono es: ", resultado)
print("O.A.R.C.")