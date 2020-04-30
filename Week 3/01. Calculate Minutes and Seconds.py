# 01 -------------
#ç# Crear una función que, a partir de un dato de entrada que sea en
# horas, nos informe cuántos minutos y cuántos segundos serían esas
# horas. Imprimir por pantalla dichos valores.
from datetime import datetime


def calculate_minutes_seconds(hours):
    hour_to_int = int(hours)
    to_minutes = 60
    to_seconds = 3600
    hours_to_min = hour_to_int * to_minutes
    hours_to_sec = hour_to_int * to_seconds
    return hours_to_min, hours_to_sec

print(calculate_minutes_seconds(20))
