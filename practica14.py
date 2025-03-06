#Practica 14: Crear una función que me devuelva el area de un triangulo (lo devuelva como valor)

def area(b, h):
    return round((b*h)/2,2)

areatriangulo = area(int(input("Dime la base:")), int(input("Dime la altura:")))
print("El area del triangulo es de", areatriangulo )