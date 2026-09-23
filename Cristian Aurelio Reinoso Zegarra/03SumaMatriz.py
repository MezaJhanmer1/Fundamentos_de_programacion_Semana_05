# 1. CREAR LA MATRIZ
# La matriz tiene 3 filas y 3 columnas.
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 2. CALCULAR LA SUMA DE CADA FILA
# Recorremos cada fila de la matriz.
# sum(fila) suma todos los números de cada fila.
sumas_filas = [sum(fila) for fila in matriz]


# 3. CALCULAR LA SUMA DE CADA COLUMNA
# zip(*matriz) permite agrupar los elementos por columnas.
# Luego sum() calcula la suma de cada columna.
sumas_columnas = [sum(columna) for columna in zip(*matriz)]


# 4. PREPARAR EL TEXTO DE LAS SUMAS DE LAS FILAS
texto_filas = f"Suma fila 0: {sumas_filas[0]} | fila 1: {sumas_filas[1]} | fila 2: {sumas_filas[2]}"


# 5. PREPARAR EL TEXTO DE LAS SUMAS DE LAS COLUMNAS
texto_columnas = f"Suma colum 0: {sumas_columnas[0]} | col 1: {sumas_columnas[1]} | col 2: {sumas_columnas[2]}"


# Imprimimos las sumas de las filas y las columnas.
print(f"{texto_filas}")     # 0: 6 | fila 1: 15 | fila 2: 24
print(f"{texto_columnas}")  # 0: 12| col 1: 15  | col 2: 18