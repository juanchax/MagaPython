# 10 -----
# Build a program that stores all letters of the alphabet. then
# deletes the vocals *ONLY* and prints out a new list *without
# modifying the original list.
#
# Escribir un programa que almacene todas las letras del abecedario
# y luego elimine las vocales y nos devuelva una lista sin las vocales,
# sin modificar la original.

import string


alphabet = list(string.ascii_lowercase)


def del_vowels (list):
    lphbt = []
    vowels = ("a", "e", "i", "o", "u")
    for x in list:
        if x not in vowels :
            lphbt.append(x)
    print(lphbt)


del_vowels(alphabet)