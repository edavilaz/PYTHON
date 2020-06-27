# métodos clase y estáticos
'''
class Pastel:
    def __init__(self,ingredientes):
        self.ingredientes = ingredientes
    def __repr__(self):
        return f"{self.ingredientes !r}"    # !r se usa con el __repr__
    @classmethod
    def Pastel_chocolate(cls):
        return cls(["Harina","Leche","Chocolate"])
    @classmethod
    def Pastel_vainilla(cls):
        return cls(["Harina","Leche","Vainilla"])
# Para imprimir el resultado de alguna clase ya no necesito crear un objeto
print(Pastel.Pastel_chocolate())
'''

# método estático se antepone @staticmethod

import math
class Pastel:
    def __init__(self,ingredientes,tamaño):
        self.ingredientes = ingredientes
        self.tamaño = tamaño
    def __repr__(self):
        return (f'Pastel({self.ingredientes},'f'{self.tamaño})')
    def area(self):
        return self.tamaño_area(self.tamaño)
    @staticmethod
    def tamaño_area(A):
        return A ** 2 * math.pi

nuevo_pastel=Pastel(["Harina","Azucar","Leche","Crema"],4)
print(nuevo_pastel.ingredientes)
print(nuevo_pastel.tamaño)
# ejecucion metodo estatico
print(nuevo_pastel.tamaño_area(5))
