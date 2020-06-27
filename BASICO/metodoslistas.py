# MÉTODOS LISTAS
# DADA LA LISTA L
L= [2,7,8,14,8,12,6]
print(max(L)) # mayor de la lista, sale 14
print(min(L)) # menor de la lista, sale 2
print(len(L)) # número de elementos de la lista, sale 7
L.append(100) # adiciona elementos a la lista
print(len(L)) # número de elementos de la lista, sale 8
print(L.count(8))  # cuenta elementos, sale 2
L.sort()    # para ordenar la lista ascendente
print(L)
L.reverse() # del ultimo al primero sin orden
print(L)
