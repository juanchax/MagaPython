# 09 -----
# Crear un programa que pregunte al usuario 5 números enteros
# y devuelva una lista con ellos.

# Verify that the input is an integer, if not, try again
def inputNumber(num):
    while True:
        try:
            usrInput = int(input(num))
        except ValueError:
            print("El dato ingresado no es un número entero. Por favor intente nuevamente. ")
            continue
        else:
            return usrInput
            break


# build the integer list, print out the contents when done
def buildList(rangex, list):
    for i in range(int(rangex)):
        intNum = inputNumber("Por favor ingrese un número entero: ")
        list.append(intNum)
    else:
        print(list)

# main program
intList = []
usrRange = 5

print("A continuación deberá ingresar" + str(usrRange) + "números enteros. "
      "/nPor favor presione la tecla 'Enter' luego de cada número.")
buildList(usrRange, intList)