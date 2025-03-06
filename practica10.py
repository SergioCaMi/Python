# Practica 10: Imprimir por separado y con un bucle, las letras de la palabra Supercalifragilisticoespialidoso, en mayusculas menos la letra a

palabra = "Supercalifragilisticoespialido"
for letra in palabra:
    if letra != 'a':
        print(letra.upper())


