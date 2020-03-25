# 05 --------
#
# Ejercicio 5: Crear una función que devuelva True si los parámetros ingresados
# son todos números, False si hay al menos uno de los parámetros ingresados que
# no es un número, y None si ninguno de los parámetros ingresados es un número.
# Imprimir resultado por pantalla.

def inputParams():

    inParams = input("Please enter your commma-separated parameters: ")


def isNumber(param):

    try:
        isInt = int(param)
        return 1
    except ValueError:
        try:
            isFloat = float(param)
            return 1
        except ValueError:
            return  0


