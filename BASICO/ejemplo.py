# llamar al módulo

from par import ciclo_pares
n=int(input("ingrese un número: "))
print("Los numeros pares hasta ",n," son: ")
for i in ciclo_pares(n):
    print (i)