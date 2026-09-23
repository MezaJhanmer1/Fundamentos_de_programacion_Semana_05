
# Definimos una matriz de 3 filas y 3 columnas (matriz cuadrada 3x3)
# Representa una lista que contiene 3 sublistas de números
matriz = [
    [1, 2, 3],  # Fila 0
    [4, 5, 6],  # Fila 1
    [7, 8, 9]   # Fila 2
]

# Creamos una lista vacía para ir guardando 
# el resultado final de la suma de cada fila
suma_filas = []

# Inicializamos el contador de control 'i' para el índice de las filas en 0
i = 0

# Bucle principal: recorremos cada fila de la matriz mientras 'i' sea menor a 3
while i < 3:

    # Variable acumuladora temporal: iniciamos la suma de la fila actual en 0
    suma = 0

    # Inicializamos el contador de control 'j' para el índice de las columnas en 0
    j = 0

    # Bucle secundario: recorremos cada columna de la fila 'i' actual
    while j < 3:

        # Accedemos a la celda en la posición [i][j] y la sumamos al acumulador
        suma += matriz[i][j]

        # Avanzamos al siguiente elemento (columna) incrementando 'j' en 1
        j += 1

    # Una vez terminadas las 3 columnas, guardamos el total acumulado en la lista
    suma_filas.append(suma)

    # Avanzamos a la siguiente fila incrementando 'i' en 1
    i += 1



# Creamos una lista vacía para ir guardando
# el resultado final de la suma de cada columna
suma_columnas = []

# Inicializamos el contador de control 'j' para el índice de las columnas en 0
j = 0

# Bucle principal: recorremos cada columna de la matriz mientras 'j' sea menor a 3
while j < 3:

    # Variable acumuladora temporal: iniciamos la suma de la columna actual en 0
    suma = 0

    # Inicializamos el contador de control 'i' para el índice de las filas en 0
    i = 0

    # Bucle secundario: recorremos cada fila verticalmente para la columna 'j'
    while i < 3:

        # Accedemos al elemento en la fila 'i' y columna 'j' actual para sumarlo
        suma += matriz[i][j]

        # Avanzamos hacia la siguiente fila de la misma columna incrementando 'i'
        i += 1

    # Al terminar de recorrer la columna actual, guardamos la suma en la lista
    suma_columnas.append(suma)

    # Avanzamos a la siguiente columna incrementando 'j' en 1
    j += 1



# 4. IMPRESIÓN Y MOSTRADO DE RESULTADOS


# Accedemos e imprimimos individualmente cada valor de la lista de suma de filas
print("Suma fila 0:", suma_filas[0],
      "| fila 1:", suma_filas[1],
      "| fila 2:", suma_filas[2])


# Accedemos e imprimimos individualmente cada valor de la lista de suma de columnas
print("Suma col 0:", suma_columnas[0],
      "| col 1:", suma_columnas[1],
      "| col 2:", suma_columnas[2])