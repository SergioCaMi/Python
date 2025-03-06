#Practica 8: Mediante un bucle que recorra y muestre la lista de los meses del año y mostrar un texto que ponga, "El primer mes del año es enero", "el segundo mes del año es febrero"
meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
orden=['primer','segundo','tercero','cuarto','quinto','sexto','septimo','octavo','noveno','décimo','undécimo','decimosegundo']
i=0
for x in meses:
    print('El ',orden[i] ,' mes del año es', x)
    i+=1