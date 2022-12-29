# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def multi(numList):
    numList = int(numList)
    numArr = [i for i in range(1, numList+1)]

    arrPrime = []
    for j in numArr:
        if j > 1:
            for n in range(2, j):
                if(j%n) == 0:
                    break
            else:
                arrPrime.append(j)

    return arrPrime

def addListPrime(numMulti, num):
    num = int(num)

    arrListPrime = []
    for i in numMulti:

        while(num % i == 0):
            num = num / i
            arrListPrime.append(i)
        else:
            continue
    print(f'Простые множители числа {num}: {arrListPrime}')


n = input('Введите натурально число: ')

numMulti = multi(n)

addListPrime(numMulti, n)