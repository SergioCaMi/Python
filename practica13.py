# Practica 13: Crear una función personalizada, que resta 4 a un numero y lo divido por 2 pero que me devuelva un texto como resultado "el resultado es x"

def resta4(a, b):
    return print("El resultado es", (a - b) / 2)


resta4(int(input("Introduce numero a:")), int(input("Introduce numero b:")))