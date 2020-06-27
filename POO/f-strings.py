# f-strings
# para dar formato a cadenas
# f format %
'''
curso = "python"
print("tutoriales de %s"%curso)     # para imprimir tipo cadenas

# más variables se colocan las variables como parametros al final
nombre= "victor"
edad=25
print("Hola soy %s y tengo %s años."%(nombre,edad))

# str.format
nombre= "victor"
edad=25
print("hola soy {} y tengo {} años.".format(nombre,edad))

# f-strings

print(f"Hola soy {nombre} y tengo {edad} años.")
'''

# otro ejemplo con clases y objeto

class Estudiante:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        # este metodo se utiliza para mostrar posteriormente solo con un print
        return f"{self.nombre}{self.apellido}{self.edad}"


# creación de objeto, entrega de parametros y posterior impresion
nuevo_estudiante = Estudiante("Victor"," cruz ",17)
print(f" {nuevo_estudiante}")