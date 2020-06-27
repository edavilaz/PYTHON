# POLIMORFISMO CON HERENCIA
class Aves:
    def volar(self):
        print ("Algunas aves pueden volar")
class Aguila(Aves):
    def volar(self):
        print("Las águilas pueden volar")
class Gallina(Aves):
    def volar(self):
        print("Las gallinas no pueden volar")
# creación de objetos
obj_ave=Aves()
obj_aguila=Aguila()
obj_gallina=Gallina()

#mostramos los atributos de los objetos creados

obj_ave.volar()
obj_aguila.volar()
obj_gallina.volar()

