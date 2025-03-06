#Practica 22: Partiendo de 4 listas, en la primera contendra las fechas en formato
# mes@dia@año, la segunda dias en numero, la tercera horas en numero, la cuarta minutos en numero.
#El objetivo es generar una lista resultante que contenga el incremento de dias, horas y minutos, de cada elemento de la lista, teniendo en cuenta el mismo numero de orden o de indice
#Lista 1       Lista 2     Lista 3      Lista 4    ->           Lista 5
#05@11@2024          8          20           18        19/05/2024 20:18

#Fechas = ["03@15@2012", "07@22@2025", "11@09@2030", "05@30@2018", "09@14@2007", "01@03@2021"]

#Días = [23, 47, 35, 12, 50, 29]
#Horas = [7, 19, 3, 22, 11, 16]
#Minutos = [42, 7, 33, 58, 21, 14]

from datetime import datetime, timedelta


fechas = ["03@15@2012", "07@22@2025", "11@09@2030", "05@30@2018", "09@14@2007", "01@03@2021"]
dias = [23, 47, 35, 12, 50, 29]
horas = [7, 19, 3, 22, 11, 16]
minutos = [42, 7, 33, 58, 21, 14]
#Creamos una lista en blanco:
fechas_finales=[]


for i in range(6):
    fecha = datetime.strptime(fechas[i], "%m@%d@%Y")
    #Pasamos un string en formato día@mes@año largo a fecha
    fechas_finales.append(fecha + timedelta(days=dias[i], hours=horas[i], minutes=minutos[i]))
    #Le aumentamos a la fecha creada con el string, x días, x horas y x minutos y lo pasamos a la lista:
    print(fechas_finales[i])