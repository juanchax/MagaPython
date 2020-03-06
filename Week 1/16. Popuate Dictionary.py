# 16 -----
#
# Create a program that creates an empty dictionary and populates it with user info
# that the user will input.
# Every time that a new datum is saved, the contents of the dictionary need to be
# printed out.
#
# Crear un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
# que se le pida al usuario.
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.


# Tupla de datos personales a pedirle a los users, agregar todos los items deseados
# Tuple containing the personal data fields that the user will be asked to fill in.
# Add any other necessary fields to the 'usr_data' tuple

usr_data = ("Name", "Age", "Gender", "Phone", "email", "Address")

# Empty dictionary
person = {}

# Iterate over the Personal Data tuple and ask the user for input
for x in usr_data:
    while usr_data.index(x) < len(usr_data):
        person[x] = input("Please enter your " + x + ": ")
        print(person)
        break