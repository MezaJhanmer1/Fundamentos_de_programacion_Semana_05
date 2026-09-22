# Crea una Lista llamada agenda
agenda = ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]

# 1. Agregar "Pedro Ruiz" al final de la Lista
agenda.append("Pedro Ruiz")

# 2. Busca en que numero de poscion esta "Carlos Díaz" y guarda en la variable posicion
posicion = agenda.index("Carlos Díaz")
# print(f"Posición de Carlos Díaz: {posicion}")  # Opcional, según requerimiento

# 3. busca dónde está "Luis Torres" con
# 4. Luego usa agenda[1] = "Luis Mendoza" para borrar el nombre antiguo y escribir encima el nuevo
pos_luis = agenda.index("Luis Torres")
agenda[pos_luis] = "Luis Mendoza"

# 5. Eliminar "Ana García"
agenda.remove("Ana García")

# Resultado final
print(agenda)