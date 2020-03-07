# 06 -----
# Create a program that calculates how much money you'll
# have after a month if you deposit $2000 in your bank
# account and the monthly interest rate is 5%. Print out the
# total.
#
# Crear un programa que calcule cuánto dinero tendré
# al cabo de un mes si deposito hoy 2000 en el banco
# y el interés mensual es de 5%, y luego devuelva por pantalla ese valor.

initial_deposit = 2000
monthly_interest = 1.05

total_upToDate = initial_deposit * (monthly_interest ** 1)

print(total_upToDate)
