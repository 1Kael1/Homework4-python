# 3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random


def arrRandom():

    array = []
    for i in range(-25,25):
        rnd_elem = random.randint(-30, 30)
        array.append(rnd_elem)

    print(f'{array}\n')
    return array

def rmv_doubble(create_arr):

    removeEl = list(set(create_arr))
    print(removeEl)

create_arr = arrRandom()

rmv_doubble(create_arr)