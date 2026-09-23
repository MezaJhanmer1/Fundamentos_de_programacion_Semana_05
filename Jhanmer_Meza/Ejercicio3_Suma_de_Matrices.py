

# Definimos una matriz de 3 filas y 3 columnas
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]



# SUMA DE LAS FILAS


# Creamos una lista vacía para guardar
# la suma de cada fila
suma_filas = []

# Recorremos las filas de la matriz
for i in range(3):

    # Iniciamos la suma de la fila en cero
    suma = 0

    # Recorremos las columnas de la fila
    for j in range(3):

        # Sumamos cada elemento de la fila
        suma += matriz[i][j]

    # Guardamos la suma de la fila
    suma_filas.append(suma)


# SUMA DE LAS COLUMNAS


# Creamos una lista vacía para guardar
# la suma de cada columna
suma_columnas = []

# Recorremos las columnas de la matriz
for j in range(3):

    # Iniciamos la suma de la columna en cero
    suma = 0

    # Recorremos las filas de la columna
    for i in range(3):

        # Sumamos cada elemento de la columna
        suma += matriz[i][j]

    # Guardamos la suma de la columna
    suma_columnas.append(suma)


# MOSTRAR LOS RESULTADOS


# Mostramos la suma de cada fila
print("Suma fila 0:", suma_filas[0],
      "| fila 1:", suma_filas[1],
      "| fila 2:", suma_filas[2])


# Mostramos la suma de cada columna
print("Suma col 0:", suma_columnas[0],
      "| col 1:", suma_columnas[1],
      "| col 2:", suma_columnas[2])

