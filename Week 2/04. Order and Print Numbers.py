# 04 -----------
#
# Ingresar 6 números por teclado, preferentemente enteros,
# ordenarlos de manera creciente e imprimirlos por pantalla.

numList = []

for i in range (6):

    number = input("Por favor ingrese un numero entero: ")
    numList.append(int(number))

# Si uso numList.sort() no me hace el sorting
# si trato de crear una nueva lista sortedList = numList.sort() me tira un exception:
# TypeError: 'NoneType' object is not iterable

#sorted(numList)
numList.sort()

for number in numList:
    print(number)