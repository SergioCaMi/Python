#Practica 16: Crear una función que compare dos numeros (a y b) y me devuelva los 3 posibles resultados en un texto, "el numero a es mayor que b", "el numero b es mayor que a"
def comparar(a,b):
    if a>b:
        print("El numero a es mayor que b", a, ">", b)
    elif a<b:
         print("El numero b es mayor que a", b, ">", a)
    else:
        print("El numero a y el numero b son iguales", b, "=", a)

comparar(float(input("Dime un numero:")),float(input("Dime otro numero:")))