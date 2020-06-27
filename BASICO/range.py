'''
range (a,b,c)
a= inicio de la lista
b= final del rango,
para la lista toma el número anterior a b
c= incremento
EJM:
range(4) -> [0,1,2,3]
range(2,6) -> [2,3,4,5]
range(3,9,2) -> [3,5,7]
'''

#TABLA DE MULTIPLICAR DEL 1 AL 10
'''
n=int(input(" Ingrese un número: "))
#range tendría que ir hasta 11
# para llegar hasta el 10
for i in range(1,11):
    print(n," x ",i," = ",n*i)
'''
# MAYOR QUE EL ANTERIOR
valor = int(input("Cuántos valores va a ingresar?: \n"))
if valor<1:
    print("error")
else:
    primero =int(input("Escriba un número: "))
    for i in range (valor -1):
        numero=int(input(f"escriba un numero mas grande que {primero} "))
        if numero <=primero:
            print(f"el {numero} no es mayor que el {primero} ")
        primero=numero
    print("gracias")