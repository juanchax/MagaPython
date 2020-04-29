# 09 ---------------
#
# Pedirle al usuario que ingrese el monto disponible en su tarjeta de crédito.
# Evaluar si puede realizar una compra de $2500, si puede indicar cuánto saldo
# le queda luego de efectuarla. Si no puede, indicar cuánto dinero le falta para
# poder realizarla.

monto_disponible = float(input('Por favor ingrese el monto disponible de su tarjeta de crédito (numeros solamente): '))

monto_compra = 2500

if monto_disponible >= monto_compra:
    print('Compra existosa, su saldo restante es: $%s' % abs(monto_disponible - monto_compra))
else:
    print('Usted no dispone de suficiente dinero para realizar la compra. Su límite de compra con el disponible actual es: $%s' % abs(monto_disponible - monto_compra))
