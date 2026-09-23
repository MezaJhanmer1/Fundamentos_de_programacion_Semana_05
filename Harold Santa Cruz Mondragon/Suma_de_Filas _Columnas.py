#Dada la matriz 3×3: [[1,2,3],[4,5,6],[7,8,9]] — Calcular y mostrar la suma de cada fila y la suma de cada columnas
matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]

# 2. CALCULAR LA SUMA DE CADA FILA
sumas_filas = [sum(fila) for fila in matriz]


# 3. CALCULAR LA SUMA 
# Luego sum() calcula la suma
sumas_columnas = [sum(columna) for columna in zip(*matriz)]
#coloca texto para mostrar las sumas de las filas y columnas
texto_filas = f"Suma fila 0: {sumas_filas[0]} | fila 1: {sumas_filas[1]} | fila 2: {sumas_filas[2]}"

texto_columnas = f"Suma colum 0: {sumas_columnas[0]} | col 1: {sumas_columnas[1]} | col 2: {sumas_columnas[2]}"


# Imprimimos las sumas de las filas y las columnas.
print(f"{texto_filas}")    

print(f"{texto_columnas}")  
