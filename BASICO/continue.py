# continue - pares
n=int(input("ingrese un número: "))
for i in range(1,n+1,1):
    if i%2==0:
        continue
        # continue salta a otra instrucción
        print (i)
    else:
        print (i)