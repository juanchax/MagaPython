# 03 -----------
#
# Pedir al usuario que ingrese por teclado 2 números, si el primero es menor
# que el segundo imprimir la resta entre el segundo y el primero, si el primero
# es mayor que el segundo imprimir la suma de ambos, y si son iguales imprimir
# su producto.


def getInput():

    # ask the user for input check that the input is a numeric value
    isInt = ''

    number = input("Please enter a number: ")
    try:
        isInt = float(number)
    except ValueError:
        print("The data entered is NOT a number, please try again. ")

    return isInt



def buildList():

     # generate a list with the user input

    numList = []

    for i in range(2):
            numList.append(getInput())

    return numList



def compareAndMaths(numList):

    num1 = numList[0]
    num2 = numList[1]

    if num1 < num2:
        print(num1 - num2)
    elif num1 > num2:
        print(num1 + num2)
    else:
        print(num1 * num2)


# main program
compareAndMaths(buildList())