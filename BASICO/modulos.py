# MÓDULOS
# MATH
'''
from math import pi
a=pi                       # da el valor de pi 3.1415....
'''
'''
from math import factorial
a=factorial(6)          # da 720
print(a)
'''
'''
from random import choice
a=choice(["cara","cruz"])       # para sacar valores aleatorios
print (a)
'''
'''
from random import randrange
a=randrange(5)        # valores aleatorios de 0 a 4
print (a)
'''
'''
from datetime import date
dia=date(2019,2,22)
año=date(2019,12,31)
fin_de_año=(año-dia).days       # para calcular los dias propiedad days
print("faltan ",fin_de_año, "días, para fin de año")
'''

from fractions import Fraction
a=Fraction(2,4)
b=Fraction(4,8)
print(Fraction(a+b))
