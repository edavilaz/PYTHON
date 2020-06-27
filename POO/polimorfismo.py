class Animales:             # clase padre
    def __init__(self,nombre):
        self.nombre= nombre
    def tipo_animal(self):
        pass         # este lo dejamos vacio porque se definirá de acuerdo al animal

class Leon(Animales):       # clase hijo
    def tipo_animal(self):
        print("Animal Salvaje")
class Perro(Animales):      # otra clase hijo
    def tipo_animal(self):
        print("Animal Doméstico")

# creación de objetos, acá se ve el polimorfismo
# ambos objetos son animales, tienen mismos atributos pero valores distintos
nuevo_animal= Leon("Simba")
nuevo_animal.tipo_animal()          # mostrará animal salvaje
nuevo_animal2 = Perro("Rex")
nuevo_animal2.tipo_animal()         # mostrará animal doméstico