# lista que contiene las notas de los estudiantes
notas = [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]

#Hacemos una variable que contara los notas aprobadas
aprobados= 0

# Calculamos el promedio:
# sum(notas) suma todas las notas y len(notas) nos indica cuantas notas hay en la lista
promedio = sum(notas) / len(notas)

# Obtenemos la nota más alta usando max()
nota_alta= max(notas)

# Obtenemos la nota más baja usando min()
nota_baja= min(notas)

# Recorremos cada nota del arreglo
for nota in notas:

    # Si la nota es mayor o igual a 11, el estudiante aprobó
    if nota >= 11:

        aprobados += 1
#Mostramos resultados
print("Promedio:",promedio)
print("Nota mas alta: ", nota_alta)
print("Nota mas baja: ", nota_baja)
print("notas aprobados: ", aprobados)



