# DICCIONARIO
'''
SON ESTRUCTURAS DE DATOS CONSISTENTES EN LISTAS DE PARES DE VARIABLES
DONDE EL 1ER. ELEMENTO SE LLAMA CLAVE(KEY) Y EL 2DO. VALOR, AMBOS PUEDEN SER DE
CUALQUIER TIPO. SE DELIMITAN POR LLAVES (KEYS)
EJEMPLO
a={"Victor":2,"Juan":3,.......}
'''

edades ={"david":30,"carlos":60,"victor":34,"hector":30}
print(edades)                   # muestra todo el diccionario
print(edades["victor"])         # muestra el valor de victor
edades["victor"]=100            # modifica el valor de 34 a 100
for i in edades:
    print(i,edades[i])          # imprime los elementos por separado con su valor respectivo