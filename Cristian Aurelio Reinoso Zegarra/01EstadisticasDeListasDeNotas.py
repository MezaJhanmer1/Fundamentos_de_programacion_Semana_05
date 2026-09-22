# Definimos la lista con las notas de los estudiantes
notas = [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]


# CALCULO DEL PROMEDIO

# sum(notas) suma todos los valores de la lista
# len(notas) cuenta cuántos elementos hay
promedio = sum(notas) / len(notas)


# max(notas) recorre la lista y devuelve el valor maximo (20)
nota_maxima = max(notas)

# min(notas) recorre la lista y devuelve el valor minimo (9)
nota_minima = min(notas)


# Se inicia la variable para saber cuantos estudiantes aprobaron
aprobados = 0

# Recorremos la lista nota por nota con un bucle 
for nota in notas:
    # Si la nota es mayor o igual a 11 (nota aprobatoria)
    if nota >= 11:
        # Si la condición se cumple, incrementamos el contador en 1
        aprobados += 1


# Mostramos los resultados
print("Promedio:", promedio)          #14.5
print("Nota mas alta:", nota_maxima)  # 20
print("Nota mas baja:", nota_minima)  # 9
print("Aprobados:", aprobados)        # 9