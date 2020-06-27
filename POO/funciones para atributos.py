# FUNCIONES PARA ATRIBUTOS

class Persona:
    edad = 27
    nombre = "victor"
    pais = "brasil"

doctor = Persona()
print(" la edad es", doctor.edad)

# getattr sirva para sacar el valor del atributo
print(" la edad es", getattr(doctor,"edad"))    # funcion para atributo geattr

# hasttr verifica si un objeto tiene un atributo
print("¿El doctor tiene una edad?", hasattr(doctor,"edad")) # dará true

# setattr sirve para cambiar el valor de un atributo
# en nombre cambiaremos de victor a hector
print("antes:",doctor.nombre)
setattr(doctor,"nombre","hector")
print("después:",doctor.nombre)

print(Persona.pais)
# delattr sirve para eliminar un objeto 
delattr(Persona,"pais")
print(Persona.pais)
