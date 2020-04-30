# 02 --------------
#
# Crear una función que devuelva una lista con todos los números
# pares del 0 al 100 inclusive. Imprimir esa lista por pantalla.

def print_evens(upper_limit):
    upper_limit = int(upper_limit)
    for number in range(0, upper_limit +1):
        if number % 2 == 0:
            print(number)

print_evens(100)
