#Dado el siguiente arreglo de notas: [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]
#Escribir un programa que calcule: promedio, nota más alta, nota más baja y cuántos aprobaron (nota ≥ 11)

#Definimos las lista de las notas

notas=[15, 18, 12, 9, 17, 14, 20, 11, 16, 13]

#colocamos el calculo de las notas

promedio=sum(notas)/len(notas)

#definimos nota_max para obtener el valor maximo de las notas

nota_max=max(notas)

#utilizamos la misma metodologia pero a la inversa obteniendo la minima

notas_min=min(notas)

#obtamos por hacer un contador de aprobados

aprobados=0

#ponemos una condicional obteniendo el numero de aprobados
for notas in notas:
 if notas >= 12 :
  aprobados=+1
#mostramos resultados

print(f"la obtencion de las notas son :{promedio}")
print(f"la nota mas alta es :{nota_max}")
print(f"la nota mas baja es :{notas_min}")
print(f"el numero de aprobados es :{aprobados}")