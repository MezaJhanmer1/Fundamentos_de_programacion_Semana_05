agenda = ["Ana Garcia", "Luis Torres", "Carlos Diaz", "Maria Lopez"]

agenda.append("Pedro Ruiz")

def buscar(lista, objetivo):
    for i, valor in enumerate(lista):
        if valor == objetivo:
            return i
    return -1
pos = buscar(agenda,"Carlos Diaz")
print(f"Encontrado Carlos Diaz en la posicion: {pos}")

agenda[1] ="Luis Mendoza"

agenda.remove("Ana Garcia")

print(agenda)