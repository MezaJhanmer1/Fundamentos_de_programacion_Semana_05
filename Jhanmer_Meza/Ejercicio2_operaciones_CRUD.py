
# Creamos una lista llamada agenda con varios nombres
agenda = [
    "Ana Garcia",
    "Luis Torres",
    "Carlos Diaz",
    "Maria Lopez"
]


# Agregamos un nuevo nombre al final de la lista
agenda.append("Pedro Ruiz")


# Creamos una función para buscar un nombre en la lista
def buscar(lista, objetivo):

    # enumerate() nos permite obtener la posición (i)
    # y el valor (valor) de cada elemento
    for i, valor in enumerate(lista):

        # Comparamos el nombre actual con el nombre que buscamos
        if valor == objetivo:

            # Si lo encuentra, devuelve su posición
            return i

    # Si termina el recorrido y no encuentra el nombre,
    # devuelve -1
    return -1


# Buscamos a Carlos Diaz dentro de la agenda
pos = buscar(agenda, "Carlos Diaz")


# Mostramos la posición donde se encontró Carlos Diaz
print(f"Encontrado Carlos Diaz en la posicion: {pos}")


# Modificamos el elemento que está en la posición 1
# Luis Torres cambia a Luis Mendoza
agenda[1] = "Luis Mendoza"


# Eliminamos a Ana Garcia de la lista
agenda.remove("Ana Garcia")


# Mostramos la agenda actualizada
print(agenda)
