# 1. Matriz dada en el enunciado
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 2. Calcular la suma de cada fila
# sum(fila) calcula la suma de los elementos de cada sublista
sumas_filas = [sum(fila) for fila in matriz]

# 3. Calcular la suma de cada columna
# zip(*matriz) transpone la matriz, agrupadola por columnas: (1,4,7), (2,5,8), (3,6,9)
sumas_columnas = [sum(columna) for columna in zip(*matriz)]

# 4. Formatear la salida para que coincida exactamente con la imagen
texto_filas = f"Suma fila 0: {sumas_filas[0]} | fila 1: {sumas_filas[1]} | fila 2: {sumas_filas[2]}"
texto_columnas = f"Suma col 0: {sumas_columnas[0]} | col 1: {sumas_columnas[1]} | col 2: {sumas_columnas[2]}"

# Impresión del resultado final
print(f"{texto_filas} || {texto_columnas}")