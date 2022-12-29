# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример:*

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def randomList(k):

    arr = []

    for i in range(0, k+1):
        rnd_el = random.randint(0, 101)
        arr.append(rnd_el)

    return arr


def polynomial(valueArr):

    acc = ''

    for i in valueArr:
        idx = valueArr.index(i)

        acc += (f'{i}*{"x"}**{idx}')

        if idx < len(valueArr)-1:
            acc += ' + '

    acc = acc + "= 0  " 
    print(acc)
    return acc


def createFile(valuePoly):
    with open('dz4-task4.txt', 'a') as poly:
        poly.write(valuePoly)
        poly.write('\n')


k = int(input('Укажите степень многочлена : '))

valueArr = randomList(k)

valuePoly = polynomial(valueArr)

createFile(valuePoly)
