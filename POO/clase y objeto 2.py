# CLASES Y OBJETOS 2
'''
class Persona:
    doctor = "victor"
Persona.doctor          # para llamar a la clase y su objeto
print(Persona.doctor)   # para mostrar en pantalla
'''
'''
class Jugadores_A:
    j1 = "messi"
    j2 = "cr7"          # j2 es un objeto y lo otro es un valor
print(Jugadores.j2)

class Jugadores_B:
    j3 = "marcelo"
    j1 = "falcao"

print(Jugadores_B.j1)
'''
# crear una clase vacía

class Nombre:
    pass                    # se utiliza para salir de la clase

# Posteriormente se puede crear objetos para incluirlos en la clase
victor = Nombre()
maria = Nombre()

# luego podemos crear los atributos para cada objeto
# objeto.atributo = valor

victor.edad = 30
victor.sexo = "Masculino"
victor.pais = "Bolivia"

maria.edad = 25
maria.sexo = "Femenino"
maria.pais = "Colombia"

# imprimir print(objeto.atributo)

print(victor.edad)
print(maria.edad)

