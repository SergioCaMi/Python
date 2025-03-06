#Practica 15: Crear una función que me pasandole como parametro un numero, mediante la función input, y que me devuelva el mes en letras correspondiente (cuidado si el numero no esta entre 1 y 12)
meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
def mes(numero):
    if numero>0 and numero<=12:
        print("El mes escogido es el", meses[numero-1])
    else:
        print("Error en el numero de mes.")

mes(int(input("Introduce el numero de un mes en números:")))