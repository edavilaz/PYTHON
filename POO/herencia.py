# herencia

class pokemon:
    pass                # clase base la creo vacia por eso el pass
    def __init__(self, nombre, tipo):   # ponemos los parametros que luego se llenarán
        self.nombre = nombre
        self.tipo = tipo

    def descripcion(self):      # con esto se mostrará el nombre y tipo
        return "{} Es un pokemon de tipo {} ".format(self.nombre,self.tipo)
# ahora crearemos una clase hijo

class pikachu(pokemon):   # se puede utilizar todo lo de la clase pokemon(padre)
    def ataque(self,tipoataque):     # creo un atributo especifico de esta clase (tipoataque)
        return "{} tipo de ataque: {}".format(self.nombre,tipoataque)

# creamos otra clase hijo
class charmander(pokemon):
    def ataque(self,tipoataque):     # creo un atributo especifico de esta clase (tipoataque)
        return "{} tipo de ataque: {}".format(self.nombre,tipoataque)

# creadas las clases y los metodos, creamos los objetos

nuevo_pokemon = pikachu("boby","electrico") # nombre y tipo como parametros
print(nuevo_pokemon.descripcion())          # acá utilizo la clase padre
print(nuevo_pokemon.ataque("impacto trueno"))   # acá utilizo la clase hijo

