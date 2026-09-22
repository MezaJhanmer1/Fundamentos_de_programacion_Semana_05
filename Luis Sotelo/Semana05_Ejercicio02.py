#Agenda de lista de personas, agregar,mostrar posic, buscar, modificar y eliminar.


agenda = ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]

agenda.append("Pedro Ruiz") #agregar al final de lista
posic_carlos = agenda.index("Carlos Díaz")   # .index() nos dice en qué posición (índice 2) está.
posic_luis = agenda.index("Luis Torres")     # Buscamos en que posicion esta Luis Torres (indice 1)
agenda[posic_luis] = "Luis Mendoza"          # agenda (1) reemplaza el dato al nuevo
agenda.remove("Ana García")                  # Eliminar

# Print
print(f"Posición de Carlos Díaz: {posic_carlos}")
print(f"Agenda final: {agenda}")