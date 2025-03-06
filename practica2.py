# Practica 2: Escribir un programa que pida un número y determine si es mayor o menor que 20
i=int(input('Pon un número:'))
print(i)
if i>20:
    print(i, "es mayor que 20")
else:
    print(i, "es menor o igual que 20")

#Practica 2 Bis: lo mismo, pero con números decimales.

i=input('Pon un número:')
print(float(i))
if float(i)>20:
    print(float(i), "es mayor que 20")
else:
    print(float(i), "es menor o igual que 20")