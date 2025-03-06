#Práctica 20: Crear una función para almacenar en una variable que se llamará semana, que después de informarle de una fecha mediante input en el formato dd-mm-aaaa (una sola variable), almacene el valor de la semana de la fecha aportada.



from datetime import date
def semanaenmes(semana):
    semanalista = semana.split('-')
    fecha = date(int(semanalista[2]), int(semanalista[1]), int(semanalista[0]))
    print("La semana del año de la fecha aportada es", fecha.strftime('%W'))

semana = input("Introduce una fecha en formato dd-mm-aaaa:")
semanaenmes(semana)

#dia, mes, año = fecha.split('-'): si no coinciden los parámetros, dará error. Hay que hacer un control de excepciones.