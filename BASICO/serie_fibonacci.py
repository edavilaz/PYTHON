# SERIE FIBONACCI 1,1,2,3,5,8,13,21,34,55....
# w=interruptor

n=int(input("Ingresa un número para sacar la serie: "))
w1=1
w2=1
s=0
c=0
if n<=0:
    print("Error")
elif n==1:
    print(w1)
else:
    while c<n:
        s=w1+w2
        print(w1, end=" , ")
        # actualizar los datos
        w1=w2
        w2=s
        c += 1  # c=c+1