# 01 ------
# Pedir al usuario que ingrese un mensaje cualquiera, si el mensaje tiene más de 100 caracteres
# imprimirlo por pantalla, si tiene entre 50 y 100 caracteres imprimirlo al revés, si no se cumple
# ninguna de las opciones anteriores, por pantalla devolver un mensaje que diga "su mensaje es demasiado corto".

def inputMessage():

    message = input("Please enter you message: ")
    messageLength = len(message)


    if messageLength > 100 :

        print(message)

    elif messageLength > 50 :

        messageReversed = ''.join(reversed(message))
        print(messageReversed)

    else:

        print("Your message is too short. ")


inputMessage()
