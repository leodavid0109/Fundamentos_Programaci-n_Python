def dias_naufragio(naufragio, rescate):
    diferencia = rescate - naufragio
    bloques = diferencia.days // 5
    rayas = diferencia.days % 5
    bloque = [5] * bloques
    raya = [1] * rayas
    conteo = bloque + raya
    return conteo

from datetime import datetime
cantidad = int(input())
for i in range(cantidad):
    caso = input()
    caso = caso.split()
    caso[0] = datetime.strptime(caso[0], "%d-%m-%Y")
    caso[1] = datetime.strptime(caso[1], "%d-%m-%Y")
    conteo = dias_naufragio(caso[0], caso[1])
    for j in range(len(conteo) - 1):
        print(conteo[j], end = " ")
    print(conteo[-1])
