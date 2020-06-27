# POLIMORFISMO CON MÉTODOS
class Colombia:
    def capital(self):
        print("Bogotá")
    def idioma(self):
        print("Español")
class Francia:
    def capital(self):
        print("París")
    def idioma(self):
        print("Francés")
# creamos los objetos
colombiano= Colombia()
frances= Francia()
# creamos los métodos
# deben tener dos o más parámteros sino dará error

for pais in (colombiano, frances):
    pais.capital()
    pais.idioma()
