#Calcular y mostrar la suma de cada fila y la suma de cada columna.

matriz = [
    [1, 2, 3],
    [4, 5, 6],  
    [7, 8, 9]   
]

total_fila = len(matriz)
total_columna = len(matriz[0])      #entra a la primera fila y cuenta cuantas columnas tiene dentro

print("--- SUMA DE FILAS ---")
for f in range(total_fila):
    suma_fila = 0      

    for c in range(total_columna):   #para variable C en el rango (3), va generar los numeros 0,1 y 2, va dar 3 vueltas y cambiara el valor
        suma_fila += matriz[f][c]    
    print(f"Suma de la Fila {f}: {suma_fila}")

print("\n--- SUMA DE COLUMNAS ---")

for c in range(total_columna):
    suma_columna = 0
   
    for f in range(total_fila):
        suma_columna += matriz[f][c]
    print(f"Suma de la Columna {c}: {suma_columna}")




    #FILAS
    #Cuando f= 0
    #Cuando c = 0: suma_fila += matriz[0][0] (Busca fila 0, columna 0, que es el 1). La alcancía ahora tiene 1.
    #Cuando c = 1: suma_fila += matriz[0][1] (Busca fila 0, columna 1, que es el 2). La alcancía ahora tiene 1 + 2 = 3.
    #Cuando c = 2: suma_fila += matriz[0][2] (Busca fila 0, columna 2, que es el 3). La alcancía ahora tiene 3 + 3 = 6.

    #Cuando f= 1
    #Cuando c = 0: suma_fila += matriz[1][0] (Fila 1, columna 0, que es el 4). La alcancía tiene 4.
    #Cuando c = 1: suma_fila += matriz[1][1] (Fila 1, columna 1, que es el 5). La alcancía tiene 4 + 5 = 3.
    #Cuando c = 2: suma_fila += matriz[1][2] (Fila 1, columna 2, que es el 6). La alcancía tiene 9 + 6 = 15.

    #COLUMNAS
    #Cuando f= 0
    #Cuando f = 0: suma_columna += matriz (Busca Fila 0, Columna 0, que es el 1). Alcancía = 1.
    #Cuando f = 1: suma_columna += matriz (Busca Fila 1, Columna 0, que es el 4). Alcancía = 1 + 4 = 5.
    #Cuando f = 2: suma_columna += matriz (Busca Fila 2, Columna 0, que es el 7). Alcancía = 5 + 7 = 12.

    #Cuando f=1
    #Cuando f = 0: suma_columna += matriz (Fila 0, Columna 1, que es el 2). Alcancía = 2.
    #Cuando f = 1: suma_columna += matriz (Fila 1, Columna 1, que es el 5). Alcancía = 2 + 5 = 7.
    #Cuando f = 2: suma_columna += matriz (Fila 2, Columna 1, que es el 8). Alcancía = 7 + 8 = 15.