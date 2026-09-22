#Calcule: promedio, nota más alta, nota más baja y cuántos aprobaron
# lista de notas
notas = [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]
aprobados = 0

promedio = sum(notas) / len(notas)  #Sacar promedio
nota_mas_alta = max(notas)
nota_mas_baja = min(notas)

for nota in notas:
    if nota >= 11:
        aprobados += 1

# Print
print(f"--- Lista de Notas ---")
print(f"Promedio de notas: {promedio:.1f}")
print(f"Nota más alta:     {nota_mas_alta}")
print(f"Nota más baja:     {nota_mas_baja}")
print(f"Total aprobados:   {aprobados} de {len(notas)}")





#aprobados = len([nota for nota in notas if nota >= 11]) #lista de comprensión 
#Por cada nota dentro de la lista de notas, conserva la nota solo si esa nota >= 11". (Esto crea una nueva lista filtrada: [15..13]
#Con el len(9) cuenta 9 elementos) - Guarda ese resultado (9) en la variable llamada aprobados.