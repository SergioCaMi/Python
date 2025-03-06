#Practica 21: Calcular los segundos transcurridos entre dos ejecuciones de celdas de Júopiter diferentes (ejecutar una celda, esperar unos segundos y al ejecutar la segunda celda, que nos diga cuantos seegundos han transcurridos).

from datetime import datetime

ahora1= datetime.now()

#Ejercicio para hacer en celdas Jupyter

ahora2 =datetime.now()

print((ahora2-ahora1))