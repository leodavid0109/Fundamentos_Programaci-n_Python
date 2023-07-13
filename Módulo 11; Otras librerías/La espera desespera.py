from datetime import datetime
cantidad = int(input())
registro = []
for i in range(cantidad):
    caso = input()
    caso = caso.split(", ")
    if caso[1] == "barberia":
        caso[2] = datetime.strptime(caso[2], "%H:%M:%S")
        caso[3] = datetime.strptime(caso[3], "%H:%M:%S")
        registro.append(caso[3] - caso[2])
tiempo = 0
for i in registro:
    tiempo += i.seconds
promedio = tiempo / len(registro)
horas = round(promedio // 3600)
minutos = round((promedio % 3600) // 60)
segundos = round((promedio % 3600) % 60)
print(len(registro), "veces")
print(f"{horas} horas, {minutos} minutos, {segundos} segundos")
