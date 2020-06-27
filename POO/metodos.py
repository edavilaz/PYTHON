# MÉTODOS
# UN MÉTODO ES UNA FUNCIÓN, SE LLAMA MÉTODO
# CUANDO SE ENCUENTRA DENTRO DE UNA CLASE
# determina una acción o un comportamiento

#class nombre de la clase
# DEF nombre del método (SELF):
# SELF.nombre de la variable = algoritmo
'''
class Matematica:
    def suma(self):         # se usa self porque aún no se creo un objeto
        self.n1 = 2
        self.n2 = 3

s=Matematica()              # creación de un objeto
s.suma()
print(s.n1+s.n2)
'''
'''
# __init__(self)
class Ropa:                     # creamos la clase
    def __init__(self):         # definimos los métodos
        self.marca = "willow"
        self.talla = "M"
        self.color = "rojo"
camisa = Ropa()                 # creamos el objeto
print(camisa.talla)             # mostramos el onjeto con un atributo
'''
# clase con parámetros

# CALCULADORA

class Calculadora:              # creamos la clase
    def __init__(self,n1,n2):   # definimos los métodos
        self.suma = n1+n2
        self.resta = n1-n2
        self.producto = n1*n2
        self.division = n1/n2
operacion = Calculadora(2,3)    # creamos el objeto e ingresamos los parametros
print (operacion.producto)





