'''

#para que la pantalla quede en pausa y se vea la información
import numpy as np
a= np.array([6,7,1,2,3])
b= np.array([6,7,5,8,1])
print(a+b)              # se puede sumar, restar, multiplicar, dividir los vectores
print(a-b)
print(a**b)             # exponente
print(a.argmax())       # da el indice del valor máximo 1, que es la posición del 7
print(a.argmin())       # da el indice del valor mínimo 2, que es la posición del 1
print(a.sum())       # da la suma de cada uno de los elementos, da 19
print(a.prod())       # da el producto de cada uno de los elementos, da 252

# MATRICES
matriz =np.array([[1,2,3],[4,5,6],[7,8,9]])
print("vector: ",a)
print("matriz: ",matriz)
'''
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a+b)

print(a.size)           # para ver el tamaño de la matriz dará 9( cantidad de elementos)