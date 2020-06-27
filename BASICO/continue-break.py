print("PARES E IMPARES")
n1=int(input(" Escribe un número: "))
n2=int(input(f"Escribe un número mayor o igual que {n1}: "))
if n2<n1:
    print(f"Escribe un número mayor o igual que {n1}: ")
else:
    for i in range(n1,n2+1,1):
        if i%2==0:
            print(i," es Par")
        else:
            print(i," es Impar")