# 13 -----
# Create a program that stores in a variable a dictionary with the different Currency names : Currency symbols
# Ask the user for a currency name and return the currency symbol if the currency exists in the dict
# or an error message if it doesn't
#
# Crear un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso
# si la divisa no está en el diccionario.


currency_sign = {"Euro": "€", "Dollar": "$", "Yen": "¥", "Pound": "£"}
usr_input = input("Por favor ingrese el nombre de la divisa que desea: ")
if usr_input.capitalize() not in currency_sign:
    print("La divisa solicitada no se encuentra en archivo. ")
else:
    print(currency_sign[usr_input.capitalize()])