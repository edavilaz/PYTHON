# ARREGLOS (VECTORES)
'''
n=int(input("Ingresa el tamaño del arreglo: "))
m=int(input(" Ingrese numero de múltiplos: "))

A=[]                                # arreglo, lo iniciamos vacío
for i in range (1,n+1,1):           # para recorrer el vector
    A.append(i*m)                   # para llenar cada elemento con la multimplicación

print(A)                            # para mostar el vector.
'''
# imprimir los números impares >3
'''
A=[1,5,8,9,30,9,13]
B=[]                        # creamos un vector que tendra los elementos

for i in A:
    if i > 3 and i%2==1:     # >3 e impares
        B.append(i)
print(B)
'''
# CALCULAR 10 NÚMEROS ALEATORIOS
import random           # importar un módulo para generar numeros aleatorios

def vector_aleatorio(n):
    vector=[0]*n                   # creacion del vector
    for i in range(n):
        vector[i]= random.randint(0,10)     #para generar numeros del 0 al 10
    return vector

n=int(input("Ingrese Cantidad de Numeros aleatorios que desea: "))

aleatorio=vector_aleatorio(n)       # llamar a la función
print(aleatorio)                    # mostrar vector resultante