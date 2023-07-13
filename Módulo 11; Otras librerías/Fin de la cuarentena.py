def tiempo(inicio, fin):
    time = fin - inicio
    dias = time.days
    horas = dias * 24
    minutos = horas * 60
    segundos = minutos * 60
    return dias, horas, minutos, segundos

from datetime import datetime
cantidad = int(input())
for i in range(cantidad):
    caso = input()
    caso = caso.split()
    caso[1] = datetime.strptime(caso[1], "%Y-%m-%d")
    caso[2] = datetime.strptime(caso[2], "%Y-%m-%d")
    dias, horas, minutos, segundos = tiempo(caso[1], caso[2])
    print(f"{dias} dias = {horas} horas = {minutos} minutos = {segundos} segundos")
