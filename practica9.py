#Practica 9: Con un bucle for recorrer la siguiente lista [5, -8, 142, 75, 62, 37, -20, 41] y clasificar los números por tramos de 30 en 30, empezando por el 0, y debe indicar un texto donde me diga "el número X está comprendido entre 0 y 30. Si no está en ningún tramo, debe decirlo.

numeros = [5, -8, 142, 75, 62, 37, -20, 41]
for numero in numeros:
    if numero >=0 and numero <= 30:
        print("El numero", numero, "está en el rango 0-30")
    elif numero >30 and numero <= 60:
        print("El numero", numero, "está en el rango 31-60")
    elif numero >60 and numero <= 90:
        print("El numero", numero, "está en el rango 61-90")
    elif numero >90 and numero <= 120:
        print("El numero", numero, "está en el rango 91-120")
    elif numero >120 and numero <= 150:
        print("El numero", numero, "está en el rango 121-150")
    else:
        print("El numero", numero, "está fuera de rango")
