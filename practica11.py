# Practica 11: Mediante una lista de numeros [28,15,32,7,44,35,62,73,19] imprimit los numeros
# por indivisual, mientras la suma de los valores impresos sea menor de 180


numeros = [28, 15, 32, 7, 44, 35, 62, 73, 19]
suma = 0
for numero in numeros:
    suma += numero
    if suma >= 180: break
    print("El nuevo numero es:", numero, "y la suma total hasta ahora es ", suma)


