# método super()

class Mamifero:
    def __init__(self,nombre):
        print(nombre,"Es un animal de sangre caliente")
class Leon(Mamifero):
    def __init__(self):
        print("El león es un animal de cuatro patas")
        super().__init__("Simba")
# sólo con haber utilizado super dentro de la clase hija
# todo saldrá con crear el objeto

nuevo_leon=Leon()

