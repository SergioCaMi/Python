#Practica 7: Mediante un bucle que recorra y muestre la lista de los meses del año y mostrar un texto que ponga, "El 1 mes del año es enero", "el 2 mes del año es febrero"
meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
i=1
for x in meses:
    print('El ',i ,' mes del año es', x)
    i+=1