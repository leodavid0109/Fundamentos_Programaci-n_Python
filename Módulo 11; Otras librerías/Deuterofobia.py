def coincidencia_lunes(nacimiento, años):
    contador = 0
    for i in range(años):
        nacimiento = nacimiento.replace(year = nacimiento.year + 1)
        if nacimiento.weekday() == 0:
            contador += 1
    return contador

from datetime import datetime
cantidad = int(input())
for i in range(cantidad):
    caso = input()
    caso = caso.split()
    caso[0] = datetime.strptime(caso[0], "%Y/%m/%d")
    caso[1] = int(caso[1])
    contador = coincidencia_lunes(caso[0], caso[1])
    print(contador)
