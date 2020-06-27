# ENCAPSULACIÓN
# Es el ocultamiento de datos del estado interno,
# para proteger la integridad del objeto

class Cliente:
    def __init__(self):
        self.__codigo=4321      # después del.__ eso hace que se encapsule
    def getcodigo(self):        # para poder mostrar el valor de la variable encapsulada.
        return self.__codigo
    def __cuenta(self):
        print("Cuenta de Procesamiento")

# para llamar encapsulados
persona= Cliente()
#print(persona.__codigo)        #dará error porque está encapsulado
# objeto._nombre clase__nombre atributo
print(persona._Cliente__codigo)     # imprime el valor
persona._Cliente__cuenta()          #dara el mensaje
