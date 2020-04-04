# 06 ------------
#
# Escribir un programa que seleccione una operación de cuatro operaciones numéricas
# disponibles, una vez seleccionada la operación, introducir dos números y ejecutar la operación.

case = int(input("Por favor seleccione una operación:"
                 "1 - Suma"
                 "2 - Resta"
                 "3 - Multiplicación"
                 "4 - División"))

if 0 > case <= 4:
    print("Ingrese dos números: ")
    num1 = int(input())
    num2 = int(input())

    if case == 1:
        print(num1 + num2)
    elif case == 2:
        print(num1 - num2)
    elif case == 3:
        print(num1 * num2)
    else:
        print(num1 / num2)
else:
    print("La opción ingresada no es válida. Por favor verifique los datos e intente nuevamente.")