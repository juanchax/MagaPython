# 14 -----
# Crear un programa que pregunte al usuario su nombre, edad, dirección y teléfono
# y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje.


def storeUsrInfo(emptyDict):

    keysUsrInfo = list(emptyDict.keys())
    for keys in keysUsrInfo:
        datum = input("Please enter your " + keys + ": ")
        emptyDict[keys] = datum
    else:
        print(emptyDict)


def buildDict(listX):

    myDict = dict.fromkeys(listX, "")
    return myDict


# List of data to ask from the user
usrInfo = ["name", "age", "address", "phone"]

storeUsrInfo(buildDict(usrInfo))