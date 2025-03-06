# Practica 23: Crearemos una serie de pandas, con los siguientes numeros [34,124,81,9,81,67,124,34,15,47,81,124,9,67,22] a esta serie le llamaremos numeros_VIP, clonaremos esta serie para tener solamente los numeros de la serie que sean mayores de 50, en orden ascendente y reindexado. a esta nueva serie le llamarenos numeros_VIP50,
# a esta nueva serie le aplicaremos una función por la cual si el numero esta entre 60-85, le sumaremos 10 y si no esta entre 60-85 le restaremos 5.
# Redondeado a 3 decimales
# Ver en un texto el promedio de la serie numeros_VIP50
# Ver en un texto la desviación tipica de a serie numeros_VIP50
# Ver en un texto la varianza de la serie numeros_VIP50
# #Normal
# Ver la suma acumulada serie numeros_VIP50

# Practica 23
import pandas as pd

# Crear la lista de numeros VIP
lista_VIP = [34, 124, 81, 9, 81, 67, 124, 34, 15, 47, 81, 124, 9, 67, 22]
numeros_VIP = pd.Series(lista_VIP)
print(numeros_VIP)
print()  # Una linea en blanco
# Clonar la serie siempre >50 y ordenado + reindexado
numeros_VIP50 = numeros_VIP[numeros_VIP > 50].sort_values(ascending=True, ignore_index=True)
print(numeros_VIP50)


# Crear la función
def modificar_numero(x):
    if x >= 60 and x <= 85:  # Dentro del tramo 60-85
        return x + 10
    else:
        return x - 5


# Reasignarle a la serie
numeros_VIP50 = numeros_VIP50.apply(modificar_numero)

print(numeros_VIP50)
# Ver los enunciados
print("El promedio es", round(numeros_VIP50.mean(), 3))
print("La desviación tipica es", round(numeros_VIP50.std(), 3))
print("El promedio es", round(numeros_VIP50.var(), 3))
# El acumulado
print("El promedio es", numeros_VIP50.cumsum())
