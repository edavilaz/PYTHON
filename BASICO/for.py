# cadenas con for
# dividir la frase numero
'''
for i in "numero":
    print(i)
'''

# CALCULAR EL NÚMERO DE VOCALES DE UNA FRASE
'''
frase= str(input("Ingrese una frase: "))
vocales= "aeiouAEIOU"
contador=0
for i in frase:
    if i in vocales:
        contador=contador +1
print(" El número de vocales es: ",contador)
'''
# ORDEN DESCENDENTE CON FOR RANGE
'''
n=int(input("Ingresa un número a ordenar descendentemente:"))
for i in range(n,0,-1):
    print(i)
'''
# ORDEN ASCENDENTE CON FOR RANGE
'''
n=int(input("Ingresa un número a ordenar ascendentemente:"))
for i in range(1,n+1,1):
    print(i)
'''
# SUMA DE LOS PRIMEROS N NUMEROS
'''
n=int(input("Ingresa un número: "))
suma=0
for i in range(1,n+1):
    suma=suma+i
print(" El resultado es: ",suma)
'''
# FACTORIAL

n=int(input("Ingresa un número: "))
fac=1
for i in range(1,n+1,1):
    fac=fac*i
print("El factorial de ",n, " es ",fac)
