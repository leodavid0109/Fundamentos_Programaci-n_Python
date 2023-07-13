def tiempo(fecha):
    unidad = 100 / 86400
    fecha = datetime.strptime(fecha, "%I:%M:%S %p")
    segundos = (fecha.hour * 3600) + (fecha.minute * 60) + fecha.second
    porcentaje = unidad * segundos
    porcentaje = round(porcentaje, 3)
    return porcentaje

from datetime import datetime
cantidad = int(input())
for i in range(cantidad):
    fecha = input()
    porcentaje = tiempo(fecha)
    print(f"Loading day ... {porcentaje}%")
