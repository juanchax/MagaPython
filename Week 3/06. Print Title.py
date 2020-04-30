# 06 -----------
#
# Crear una función que devuelva por pantalla un mensaje ingresado
# por parámetro pero en modo Title. Si el mensaje ya está en modo
# title, que devuelva por pantalla "El mensaje ya está en modo title: {mensaje}"

def to_title(message):
    count_is_title = 0
    word_count = len(message.split(' '))
    word_list = list(message.split(' '))
    if word_count == 1 and message.istitle():
        print('El mensaje ya está en modo title: %s' % (message))
    elif word_count == 1 and not message.istitle():
        print(message.title())
    else:
        for word in word_list:
            if word.istitle():
                count_is_title += 1
        if count_is_title == word_count:
            print('El mensaje ya está en modo title: %s' % (message))
        else:
            print(message.title())

message = 'Hola como Te Va'

to_title(message)
