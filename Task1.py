# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math 
from decimal import Decimal


def calcLevel(d):

    arr1 = [0 for i in range( int(d) )]
    
    number = ''
    for i in arr1:
        number +=str(i)
    number = '1.'+number

    return number


def calcPi(numlevel):
    num = Decimal( math.pi)
    print(f'Число π (Без точности в кол-ве знаков): {num}')

    numOut = num.quantize( Decimal(numlevel) )
    print(f'Число π (C точностью до {len(numlevel)-2} знаков): {numOut}')



d = input("Укажите точность (кол-во знаков после запятой ) : ")
numlevel = calcLevel(d)

calcPi(numlevel)