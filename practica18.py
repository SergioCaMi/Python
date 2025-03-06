#Practica 18: Crear una función para que pasandole por separado, el dia, el mes y el año nos devuelva un texto que ponga "la diferencia de dias entre hoy y la fecha informada yyyy/mm/dd es de X dias", siempre y cuando la fecha informada sea mas antigua que hoy
from datetime import date
def diferenciadias(dia, mes, ano):
    fecha1 = date(ano, mes, dia)
    fecha2 = date.today()
    if fecha2<fecha1:
        print("la fecha aportada debe ser anterior a hoy")
    else:
        print(fecha1, "-", fecha2)
        dias = fecha2 - fecha1
        print("Han pasado",(fecha2 - fecha1).days, "dias.")

dia = int(input("Introduce un día del año: "))
mes = int(input("Introduce un mes del año: "))
ano = int(input("Introduce un año: "))
diferenciadias(dia, mes, ano)
