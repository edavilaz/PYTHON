# serie A B A B A B A .....
n=int(input("Ingrese un número: "))
for i in range(1,n+1,1):
    if i%2==1:
        print ("A",end=" ")
    else:
        print ("B",end=" ")