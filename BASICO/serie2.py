# SERIE 4,3,2,1,4,3,2,......
# C= CONTROLADOR
# W= INTERRUPTOR

n=int(input("Ingresa un número: "))
c=0
w=4
while c<n:
    print(w,end= " , ")
    if w>1:
        w=w-1
    else:
        w=4
    c=c+1