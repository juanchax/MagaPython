'''

# 01 -----
# Imprimir en pantalla "Hola Mundo!"

print("Hola Mundo!")


# 02 -----
# Crear un programa en el cual se almacene en una variable el string "Hola Mundo!"
# y luego se imprima por pantalla dicha variable.

texto = "Hola Mundo!"
print(texto)


# 03 -----
# Crear un programa que pregunte al usuario su nombre y edad
# y luego imprima esos datos en renglones distintos.

nombre = input("Por favor ingrese su nombre: ")
edad = input("Por favor ingrese su edad: ")

print(nombre)
print(edad)


# 04 -----
# Crear un programa que pregunte al usuario su nombre y devuelva "¡Hola {nombre}!"

nombre = input("Por favor ingrese su nombre: ")
print("¡Hola " + nombre + "!")


# 05 -----
# Crear un programa que pida al usuario ingresar 2 números por teclado
# y devuelva por pantalla la suma de ellos en un renglón,
# la resta en otro, el producto en otros y la división en otro.

print("A continuación se le pedirá que ingrese dos números.")
number_1 = int(input("Por favor ingrese el primer número: "))
number_2 = int(input("Por favor ingrese el segundo número: "))

print(number_1 + number_2)
print(number_1 - number_2)
print(number_1 * number_2)
print(number_1 / number_2)


# 06 -----
# Crear un programa que calcule cuánto dinero tendré
# al cabo de un mes si deposito hoy 2000 en el banco
# y el interés mensual es de 5%, y luego devuelva por pantalla ese valor.

initial_deposit = 2000
monthly_interest = 1.05

total_upToDate = initial_deposit * (monthly_interest ** 1)

print(total_upToDate)


# 07 -----
# Crear un programa que calcule el sueldo bruto de una persona que trabaja de lunes a viernes 8 hs
# y su pago por hora es de 400 pesos.
# Devolver el sueldo por pantalla.

hourly_rate = 400
weekly_hours = 8 * 5
weeks_month = 4
salary = weekly_hours * weeks_month

print(salary)



# 08 -----
# Crear un programa que almacene en una lista las siguientes materias:
# Historia, Matemática, Lengua y Geografía.
# Luego devolver por pantalla la última materia almacenada.

list_a = ["Historia", "Matemática", "Lengua", "Geografía"]
print(list_a[-1])


# 09 -----
# Crear un programa que pregunte al usuario 5 números enteros
# y devuelva una lista con ellos.

print("A continuación deberá ingresar 5 números enteros. /nPor favor presione la tecla 'Enter' luego de cada número.")


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


# 10 -----
# Escribir un programa que almacene todas las letras del abecedario
# y luego elimine las vocales
# y nos devuelva una lista sin las vocales, sin modificar la original.

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



# 11 -----
# Crear una lista con varios números,
# luego ordenarlos de manera creciente
# y devolver por pantalla la lista ordenada
# y cuál es el menor y cuál el mayor.

num_list = [1, 3, 5, 56, 34, 78, 2, 87, 33, 4576, 231, 4, 50, 1239, 345, 76986, 90]
print(sorted(num_list))
print(min(num_list))
print(max(num_list))




# 12 -----
# Crear un programa que almacene los vectores (1,2,3) y (-1,0,2)
# en dos listas y muestre por pantalla su producto escalar



XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX




# 13 -----
# Crear un programa que guarde en una variable
# el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
# pregunte al usuario por una divisa
# y muestre su símbolo o un mensaje de aviso
# si la divisa no está en el diccionario.


currency_sign = {"Euro": "€", "Dollar": "$", "Yen": "¥", "Pound": "£"}
usr_input = input("Por favor ingrese el nombre de la divisa que desea: ")
if usr_input.capitalize() not in currency_sign:
    print("La divisa solicitada no se encuentra en archivo. ")
else:
    print(currency_sign[usr_input.capitalize()])

'''


# 14 -----
# Crear un programa que pregunte al usuario su nombre, edad, dirección y teléfono
# y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje.


'''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''


# 15 -----
# Crear un programa que almacene el diccionario con los créditos de las asignaturas de un curso
# {'Matemáticas': 6, 'Física': 4, 'Química': 5}
# y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos,
# donde <asignatura> es cada una de las asignaturas del curso,
# y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

creds_asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
keys_asignaturas = list(creds_asignaturas.keys())

for keys in keys_asignaturas:
    print(keys + " tiene " + str(creds_asignaturas[keys]) + " créditos.")

print("Total de créditos: " + str(sum(creds_asignaturas.values())))

# 16 -----
# Crear un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
# que se le pida al usuario.
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.


# Tupla de datos personales a pedirle a los users, agregar todos los items deseados
datos_personales = ("Nombre", "Edad", "Genero", "Telefono", "email", "Direccion")

# Diccionario vacío
person = {}

for x in datos_personales:
    while datos_personales.index(x) < len(datos_personales):
        person[x] = input("Por favor ingrese su " + x + ": ")
        print(person)
        break
