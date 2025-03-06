# Practica 1: Crear una lista con los meses de enero a junio (excepto abril). Luego:
#    - Añadir julio y agosto.
#    - Insertar abril en su lugar correcto.
#    - Añadir marzo y junio al final.
#    - Eliminar los elementos desordenados.
#        - Respuesta:
            
            
listaMeses = ["Enero", "Febrero", "Marzo", "Mayo", "Junio"]
print(listaMeses)
listaMeses.append("Julio")
listaMeses.append("Agosto")
print(listaMeses)
listaMeses.insert(3, "Abril")
print(listaMeses)
listaMeses.append("Marzo")
listaMeses.append("Junio")
print(listaMeses)
del listaMeses[8:9]
print(listaMeses)
   