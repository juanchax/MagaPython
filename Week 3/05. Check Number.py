# 05 --------
#
# Ejercicio 5: Crear una función que devuelva True si los parámetros ingresados
# son todos números, False si hay al menos uno de los parámetros ingresados que
# no es un número, y None si ninguno de los parámetros ingresados es un número.
# Imprimir resultado por pantalla.

def inputParams():

    # function to get input and build a list of input parameters
    # with leading and trailing spaces stripped

    inParams = input("Please enter your commma-separated parameters: ")

    # build param list
    inParamsList = inParams.split(',')

    # build list with trimmed trailing and leading spaces
    paramsList = []
    for i in inParamsList:
        paramsList.append(i.strip())

    return paramsList


def isNumber(param):

    # function to check if a certain parameter
    # is a number (integer or float)

    try:
        isInt = int(param)
        return 1
    except ValueError:
        try:
            isFloat = float(param)
            return 1
        except ValueError:
            return  0


def buildTrueFalseList(paramList):

    # build list with '1' for TRUE and '0' for FALSE

    listTorF = []
    for i in paramList:
         listTorF.append(isNumber(i))

    return listTorF


def printResult(boolList):

    # function to check if the params are all, some or
    # none numeric values

    if len(boolList) == sum(boolList):
        print("True")

    elif sum(boolList) == 0:
        print("None")

    else:
        print("False")


# Main program

inList = inputParams()
checkedList = buildTrueFalseList(inList)
printResult(checkedList)

