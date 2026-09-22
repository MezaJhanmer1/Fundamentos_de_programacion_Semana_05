# 1. Definición del arreglo de notas según el enunciado
notas = [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]

# 2. Cálculo del promedio:
# sum(notas) obtiene la suma total de las notas (145)
# len(notas) obtiene la cantidad total de elementos (10)
promedio = sum(notas) / len(notas)

# 3. Obtención de la nota más alta y más baja:
# max() retorna el valor máximo de la lista
# min() retorna el valor mínimo de la lista
nota_maxima = max(notas)
nota_minima = min(notas)

# 4. Conteo de aprobados (nota mayor o igual a 11):
# Recorremos la lista y contamos 1 por cada nota que cumpla la condición
aprobados = sum(1 for nota in notas if nota >= 11)

# 5. Impresión de resultados formateados
print(f"Promedio: {promedio} | Máj: {nota_maxima} | Mín: {nota_minima} | Aprobados: {aprobados}")