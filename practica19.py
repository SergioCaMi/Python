#Practica 19:Crear una función con 3 parámetros, a los que le daremos valor mediante inputs y que corresponderán a día, mes y año. La función nos debe devolver un texto con la fecha en formato mm/dd/aa.
from datetime import date
def fechacorta(dia, mes, ano):
    fecha = date(ano, mes, dia)
    print("La fecha es",fecha.strftime('%m/%d/%y'))

fechacorta(int(input("Introduce día:")), int(input("Introduce mes:")), int(input("Introduce año:")))

