# DICCIONARIO FUNCIONES
notas = {"david":85,"carlos":60,"victor":98,"hector":75}

print(str(notas))           # muestra todo el diccionario como cadena
print(type(notas))          # muestra  el tipo diccionario
#print(notas.clear)          # eliminar todos los elementos
notas2= notas.copy()        # para copiar un diccionario a otro
print(notas2)
nota3 = dict.fromkeys(["david","carlos","victor","hector"],100)
print(nota3)                # para dar el mismo valor a diferentes claves
valor=notas.get("victor")
print(valor)                # da el valor de la clave que se ingresa como parametro

items= notas.items()        # regresa la lista de pares (clave, valor)
print(items)

keys = notas.keys()         # regresa una lista con las claves
print(keys)

values = notas.values()     # regresa una lista con los valores
print(values)

dic1 = {"a":1,"b":2,"c":3,"d":4}
dic2 = {"d":5,"e":6,"f":7,"g":8}
dic1.update(dic2)           # sirve para añadir los elementos del dic2 al dic1
print (dic1)                # OJO los elementos del dic 2 actualizan valores del dic1 "d":5
