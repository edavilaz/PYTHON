# break - pares
n=int(input("ingrese un número: "))
for i in range(1,n+1,1):
    if not(i%2) & (i%6) :
        continue
    if i%6 ==0:
        break
    print (i)