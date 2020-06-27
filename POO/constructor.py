# MÉTODO CONSTRUCTOR

class Persona:
    pass                            #creamos la clase, con pass si no tiene datos
    def __init__(self,nombre,año):      # creamos los distintos metodos
        self.nombre = nombre
# se pone el mismo valor que el parámetro para que cambie con la entrega de parametros
        self.año = año
    def descripcion(self):
        return "{} tiene {} años".format(self.nombre, self.año)
    def comentario(self, frase):
        return "{} dice: {}".format(self.nombre,frase)

# creamos un objeto
doctor = Persona("Enrique", 25)      # acá creamos el objeto con los parámetros deseados

# llamamos los metodos constructores
print(doctor.descripcion())         # vacio porque no tiene parámetros
print(doctor.comentario("Me gusta el Volleyball")) # acá si ponemos un parámetro (frase)

#MODIFICAR UN ATRIBUTO
class Email:
    def __init__(self):
        self.enviado=False
    def enviar_correo(self):
        self.enviado = True
# creamos el objeto

mi_correo = Email()
print(mi_correo.enviado)
mi_correo.enviar_correo()
print (mi_correo.enviado)
