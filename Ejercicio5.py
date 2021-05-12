#definicion de variables u otros
#Datos de entrada
print("Ejercicios de examen")
o=int(input("Nota 1 Unidad:"))
r=int(input("Nota 2 Unidad:"))
a=int(input("Nota 3 Unidad:"))
c=int(input("Nota trabajo final:"))
  #Proceso
Nota=((o*20)/100)+((r*15)/100)+((a*15)/100)+((c*50)/100)
  #Datos de Salida
print("La nota final es: ", Nota)
#Proceso
if Nota>0:
  print("el ejercicio es correcto")
elif Nota<0:
  print("el ejercicio es incorrecto")
print("O.A.R.C.")