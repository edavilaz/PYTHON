# FUNCIÓN PARA SEPARAR LISTAS
# pares e impares

ejemplo=[3,7,8,9,10,5,3,7,12]

def separar_lista(L):
    L.sort()    # método utilizado para ordenanr la lista en forma ascendente
    pares=[]    # creamos las lista que contendran los pares e impares respectivamente
    impares=[]
    for i in L:
        if i%2==0:  #para sacar los pares
            pares.append(i)     #Para adicionar a la lista pares
        else:
            impares.append(i)   #Para adicionar a la lista impares
    return pares,impares        # Para retornar las listas

pares, impares= separar_lista(ejemplo)      #llamado de función
print (pares, " Estos son lo elementos pares.")
print (impares, " Estos son los elementos impares.")

print (pares,impares)