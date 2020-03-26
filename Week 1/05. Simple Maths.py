# 05 -----
# Create a simple program that asks the user for two integers
# then print out the four basic maths operations (one per line)
# Crear un programa que pida al usuario ingresar 2 números por teclado
# y devuelva por pantalla la suma de ellos en un renglón,
# la resta en otro, el producto en otros y la división en otro.

print("You will be asked to enter two integers. Press 'Enter' to begin. "
      "\nA continuación se le pedirá que ingrese dos números enteros. Presione 'Enter' para comenzar.\n")
number_1 = int(input("Please enter the first integer \nPor favor ingrese el primer número: "))
number_2 = int(input("Please enter the second integer \nPor favor ingrese el segundo número: "))

print("Addition // Suma: " + str(number_1 + number_2))
print("Substraction // Resta: " + str(number_1 - number_2))
print("Multiplication // Multiplicación: " + str(number_1 * number_2))
print("Division // División: " + str(number_1 / number_2))