# 07 ------------
#
# Crear una función que verifique si una palabra es un palíndromo o no.
# En caso de que lo sea devolver por pantalla "La palabra es un palíndromo",
# en caso contrario, devolver "La palabra no es un palíndromo".

def reverse_string(word):
    word_to_reverse = word
    word_to_list = list(word_to_reverse)
    word_to_list.reverse()
    word_reversed = ''.join(word_to_list)
    if word_reversed == word:
        return 'La palabra es un palíndromo.'
    else:
        return 'La palabra no es un palíndromo.'

print(reverse_string('momamom'))
