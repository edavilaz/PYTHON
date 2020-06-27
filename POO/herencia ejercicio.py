# herencia ejercicio práctico

class Calculadora:
    def __init__(self,numero):          # método para ingresar datos
        self.n=numero
        self.datos=[0 for i in range(numero)] # numero que será el parametro a usar
    def ingresardato(self):             # método para llamar datos
        self.datos=[int(input("Ingresar datos: "+str(i+1) + " = "))for i in range(self.n)]
# se usa.n porque es el atributo que se usará del primer método

# ahora crearemos una clase hijo

class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)        # llamamos a la clase principal y se da 2
                                            # porque son 2 numeros los necesarios
    def suma(self):
        a,b,= self.datos
        s=a+b
        print ("el resultado es: ",s)

    def resta(self):
        a,b,= self.datos
        r=a-b
        print ("el resultado es: ",r)

    def producto(self):
        a,b,= self.datos
        p=a+b
        print ("el resultado es: ",p)

    def division(self):
        a,b,= self.datos
        d=a+b
        print ("el resultado es: ",d)

class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)
# llamamos a la clase padre y damos 1 sólo un dato de entrada

    def cuadrada(self):
        import math
        a, =self.datos
        print ("El resultado es: ",math.sqrt(a))    # atributo de math para la raiz

# para comenzar a usar el programa
'''
ejemplo =op_basicas()
print(ejemplo.ingresardato())
print(ejemplo.suma())

ejemplo2= raiz()
print(ejemplo2.ingresardato())
print(ejemplo2.cuadrada())
'''
# FUNCIONES DE PRUEBAS

objeto= op_basicas()

# verifica la herencia True - False
# como parametros, recibe el (objeto, clase a la que pertenece)
print(isinstance(objeto,op_basicas))    # dará True
print(isinstance(objeto,raiz))          # dará False

# issubclass verifica herencia de clase
# (clase Hijo, clase Padre)

print(issubclass(Calculadora,op_basicas))
# dara False, porque como 1er. pusimos a la clase padre
print(issubclass(op_basicas,Calculadora))
# dará True primero se pone la clase hijo, clase padre
# la subclase op_basicas, es hija de la Clase Calculadora(padre)

