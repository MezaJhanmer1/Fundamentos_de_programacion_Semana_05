#Tienes la agenda: ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]
#Realiza: (1) Agregar "Pedro Ruiz", (2) Buscar "Carlos Díaz" y mostrar posición, (3) Modificar "Luis Torres" por "Luis Mendoza", (4) Eliminar "Ana
#García".

#Definimos la lista de contactos

agenda=["Ana García", "Luis Torres", "Carlos Díaz", "María López"]
#[1. Agregar]
#agregamos un nuevo contacto a la lista
agenda.append("Pedro Ruiz")
#[2. Buscar]
#buscamos el contacto "Carlos Díaz" y mostramos su posición
posicion=agenda.index("Carlos Díaz")
#[3. Modificar]
#modificamos el contacto "Luis Torres" por "Luis Mendoza"
agenda[1]="Luis Mendoza"
#[4. Eliminar]
#eliminamos el contacto "Ana García" de la lista
agenda.remove("Ana García")
#mostramos los resultados
print(f"Agenda actualizada: {agenda}")
#mostramos la lista 
print(f"la lista de contactos es :{agenda}")


