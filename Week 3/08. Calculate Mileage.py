# 08 ------------
#
# Crear una función que calcule cuántos litros de nafta gasta un auto que consume
# 2 litros x 100km, en un viaje ida y vuelta MdP-Bue si la distancia es de 400km.
# Luego crear una función que, a partir de esos datos, devuelva cuánto significa
# eso en pesos si el litro de nafta está 60$

def total_gas(distance, litres_per_100km):
    total_gas = (distance * 2) / 100  * litres_per_100km # Round trip distance gas needed
    return total_gas

def total_gas_cost(distance, gas_cost, litres_per_100km):
    total_trip_cost = total_gas(distance, litres_per_100km) * gas_cost
    return total_trip_cost

# Define one way distance, litres per 100km and the cost per litre
distance_in_km = 400
cost_of_litre = 60
litres_per_100km = 2

print(total_gas_cost(distance_in_km, cost_of_litre, litres_per_100km))
