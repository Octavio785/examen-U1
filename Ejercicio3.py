#definicion de variables u otros
print("Ejercicios de examen")
bono=0
#Datos de Entrada
o=int(input("Sexo de la persona 1 si es hombre y 2 si es mujer:"))
a=int(input("Edad de la persona:"))
#Proceso
if a>=70:
  print("Se le pone la tipo C")
elif a>16 and o==2:
  print("Se le pone la tipo B")
elif a>16 and o==1:
  print("Se le pone la tipo A")
elif a<=16:
 print("Se le pone la tipo A")
print("O.A.R.C.")