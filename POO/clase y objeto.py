# CLASE

class Auto:             # primera letra mayúscula siempre.
    marca  = ""
    modelo = 0          # se crean los atributos de la clase vacios
    placa  = ""

# OBJETO
taxi = Auto()       # creación del objeto taxi
# mostramos el atributo modelo del taxi creado
# mostrará lo que está en la clase, mientras
# no le ingresemos uno nuevo
print(taxi.modelo)      # mostrará 0
