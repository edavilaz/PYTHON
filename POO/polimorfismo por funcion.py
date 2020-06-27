# POLIMORFISMO POR FUNCIÓN
class Tomate:
    def tipo(self):
        print("Vegetal")
    def color(self):
        print("Rojo")
class Manzana:
    def tipo(self):
        print("Fruta")
    def color(self):
        print("Verde")
# ahora crearemos la función está fuera de las clases

def funcion(objeto):
    objeto.tipo()       # especificamos los atributos del objeto
    objeto.color()

# Creamos los objetos
nuevo_tomate= Tomate()
nueva_manzana= Manzana()
# llamamos las funciones
funcion(nuevo_tomate)       # dará vegetal rojo
funcion(nueva_manzana)      # dará fruta verde
