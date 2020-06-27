# PROPIEDADES
class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre  # estamos encapsulando con __
        self.__salario = salario

    # el metodo get para tener acceso a las variables encapsuladas
    def getnombre(self):
        return self.__nombre

    def getsalario(self):
        return self.__salario

    # el metodo set para cambiar valores
    def setnombre(self,nombre):
        self.__nombre = nombre

    def setsalario(self,salario):
        self.__salario = salario

    # métodos para elimniacion (del), no necesita tener parametros

    def delnombre(self):
        del self.__nombre

    def delsalario(self):
        del self.__salario
# Propiedades
nombre = property(fget= getnombre(),
                  fset= setnombre(),
                  fdel= delnombre(),
                  doc="soy la propiedad del nombre")

salario = property(fget=getsalario(),
                   fset=setsalario(),
                   fdel=delsalario(),
                   doc="soy la propiedad del salario")
# creamos el objeto

empleado_uno = Empleado("Victor", 1500000)
empleado_uno.nombre = "juan"

print(empleado_uno.nombre, empleado_uno.salario)
help(empleado_uno)
