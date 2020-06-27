# del & in
curso ="python"             #cadena
lista_nueva= list(curso)    #convertimos a lista
print(lista_nueva)          # dará ['p','y','t','h','o','n']

#del
del lista_nueva[0]          # para borra un elemento de la lista
print(lista_nueva)          # dará ['y','t','h','o','n']

#in
print('y' in curso)         # dará true, en caso contrario false
print('y' in lista_nueva)