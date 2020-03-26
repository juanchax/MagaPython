# 02 ------------
#
# Crear una lista con 10 números enteros cualquiera. Indicar cuál es el número mayor
# y cuál es el número menor. Si al menos hay 3 números mayores a 100, imprimir esos
# números, si no, imprimir los números menores a 50 que formen parte de la lista.

from random import seed
from random import randint

def randNumber():

    # generate a list of 10 integers

    numbList = []
    seed(1)
    upperBound = randint(0, 1000)

    for i in range (10):
        randomx = randint(0, upperBound)
        numbList.append(randomx)

    return numbList


def printHiLo(intList):

    # sort and print the largest and smallest numbers

    print("Largest number in the list: " + str(max(intList)))
    print("Smallest number in the list: " + str(min(intList)))


def countOver100(intList):

    # count how many numbers over 100 are in the list

    count = 0

    for i in intList:
        if i > 100:
            count += 1
        else:
            continue

    return count


def printNumbers(intList):

    # print number over 100 if the count is over 3
    # or print all numbers smaller than 50 if not

    count = countOver100(intList)

    if count >= 3:
        for i in intList:
            if i > 100:
                print(i)
            else:
                continue
    else:
        for i in intList:
            if i < 50:
                print(i)
            else:
                continue


# main program

intList = randNumber()
printHiLo(intList)
printNumbers(intList)