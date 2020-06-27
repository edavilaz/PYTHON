# número positivo o negativo
'''
a=int(input(" Ingresa un número: "))
if a>=0:
    print ("Positivo")
else:
    print("Negativo")
'''
# mayor de dos números
'''
a=int(input("valor a: "))
b=int(input("valor b: "))
if a>b:
    print ("a es mayor que b")
else:
    print ("a es menor que b")
'''
# numero par o impar
# acá también se ve las formas de imprimir un resultado.
'''
a=int(input("Ingresa un número: "))
if a%2==0:
    print("El número " +str(a) + " es par")
    print ("El número {} es par". format(a))
else:
    print(a,"Es un número impar")
'''
# elif
# número neutro, negativo o positivo
# con if
'''
a= int(input(" Ingresa un número: "))

if a<0:
    r="Negativo"
else:
    if a==0:
        r="Neutro"
    else:
        r="Positivo"
print ("El numero es: ",r)
'''
# elif
'''
a= int(input(" Ingresa un número: "))

if a<0:
    r="Negativo"
elif a==0:
    r="Neutro"
else:
    r="Positivo"
print ("El numero es: ",r)
'''
# calificacion de notas
n=float(input("Ingrese su nota: "))
if n<=50.9:
    r="Reprobado"
elif n<=80:
    r="Aprobado"
elif n<=90:
    r="Sobresaliente"
else:
    r="Excelente"
print("su nota: ", n, r)