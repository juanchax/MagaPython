# 05 -----------
#
# Crear un diccionario con los meses del año de la forma { 1: "enero"}.
# Desafío: lograr cambiar las claves. Pista: si imprimen ítems del diccionario
# les crea una lista. Una vez que lo logren, imprimir el diccionario modificado.
import random

months_of_year = \
    {1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
     5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
     9: "septiembre", 10: "octubre", 11: "noviembre",
     12: "diciembre"}

def shuffle(months):
    months_shuffled = {}
    months_list = list(months.values()) # Build list from the dict's values
    months_number_list = months.keys() # Get the dict's keys to shuffle them
    months_number_shuffled = random.sample(months_number_list, len(months_number_list)) # Shuffle keys
    for month_number in months_number_shuffled:
        months_shuffled[month_number] =  months_list[months_number_shuffled.index(month_number)] # Add the shuffled keys (same value order)
    return months_shuffled

def reverse(months):
    months_reversed = {}
    months_list = list(months.values()) # Build list from the dict's values
    months_number_list = list(months.keys()) # Get the dict's keys to shuffle them
    months_number_list.reverse()
    for month_number in months_number_list:
        months_reversed[month_number] =  months_list[months_number_list.index(month_number)] # Add the reversed keys (same value order)
    return months_reversed

print(shuffle(months_of_year))
print(reverse(months_of_year))
