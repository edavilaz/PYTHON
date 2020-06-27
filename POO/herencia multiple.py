# HERENCIA MULTIPLE
# Se refiere a la posibilidad de crear una clase
# a partir de multiples clases superiores

class Telefono:
    def __init__(self):
        pass
    def Llamar (self):
        print(" Llamando...")
    def Ocupado (self):
        print(" Ocupado...")

class Camara:
    def __init__(self):
        pass
    def Fotografia (self):
        print(" Tomando Fotos...")

class Reproduccion:
    def __init__(self):
        pass
    def Reproduccion_musica (self):
        print(" Reproduciendo Música...")
    def Reproduccion_video (self):
        print(" Reproduciendo Video...")

# ahora crearemos la clase con herencia múltiple

class Smartphone(Telefono,Camara,Reproduccion):
# utilizamos def del para optimizar el uso de memoria (se borra inmediatamente la clase)
    def __del__(self):
        print("Teléfono Apagado...")

# ahora creamos el objeto

movil= Smartphone()
# print(dir(movil))   # sirve para ver los metodos que puedo utilizar con el objeto
print(movil.Llamar())
