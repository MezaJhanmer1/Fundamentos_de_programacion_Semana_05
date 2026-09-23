#  CREAMOS LA LISTA INICIAL DE CONTACTOS
agenda = ["Ana Garcia", "Luis Torres", "Carlos Diaz", "Maria Lopez"]


# 1. CREATE: AGREGAR UN NUEVO CONTACTO
# append() agrega "Pedro Ruiz" al final de la lista.
agenda.append("Pedro Ruiz")


# 2. READ: BUSCAR UN CONTACTO
# index() busca "Carlos Diaz" y devuelve su posición.
pos = agenda.index("Carlos Diaz")


# 3. UPDATE: MODIFICAR UN CONTACTO
# La posición 1 corresponde a "Luis Torres".
# Reemplazamos ese nombre por "Luis Mendoza".
agenda[1] = "Luis Mendoza"


# 4. DELETE: ELIMINAR UN CONTACTO
# remove() elimina "Ana Garcia" de la lista.
agenda.remove("Ana Garcia")



# Mostramos en pantalla la posicion encontrada.
print(f"Posicion de Carlos Diaz: {pos}")  #2

# Imprimimos la agenda después de realizar todas las operaciones.
print(agenda)      # ['Luis Mendoza', 'Carlos Diaz', 'Maria Lopez', 'Pedro Ruiz']