def asesino_serial(fechas):
    for i in range(len(fechas) - 2):
        if (fechas[i + 1] - fechas[i]) != (fechas[i + 2] - fechas[i + 1]):
            return False
    delta = fechas[1] - fechas[0]
    dias_delta = delta.days
    fecha = fechas[-1] + delta
    return dias_delta, fecha

from datetime import datetime
from datetime import timedelta
cantidad = int(input())
for i in range(cantidad):
    caso = input()
    caso = caso.split(", ")
    nombre = caso[0]
    registros = int(caso[1])
    fechas = []
    for j in range(registros):
        fechas.append(datetime.strptime(input(), "%Y-%m-%d"))
    if asesino_serial(fechas):
        delta = fechas[1] - fechas[0]
        dias_delta = delta.days
        fecha = fechas[-1] + delta
        fecha_final = fecha.strftime("%Y-%m-%d")
        print(nombre, "ataca cada", dias_delta, "dias y volvera a hacerlo en", fecha_final)
    else:
        print(nombre, "no es asesino(a) serial periodico")
    if i != cantidad - 1:
        print("")
