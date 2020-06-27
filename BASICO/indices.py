#INDICES
'''
curso='PYTHON'
print(curso[2])             # imprimirá la letra T (-> comienza en 0)
print(curso[-4])            # imprimirá la letra T (<- comienza en -1)
'''
'''
cadena= "constitucionalmente"
print(cadena[1:5])          # imprimirá del 1 al 4, (anterior al 5) onst
print(cadena[2:])          # imprimirá del 2 al final, nstitucionalmente
print(cadena[:7])          # imprimirá del principio al 6 (anterior a 7)
'''

cadena= "aeiou"
vocales=list(cadena)      # convertimos de tipo cadena a lista (tuple - para convertir en tupla)
print(vocales)
print(vocales.index("i"))  # la función index, encontrar el indice del dato buscado "". dará 2
