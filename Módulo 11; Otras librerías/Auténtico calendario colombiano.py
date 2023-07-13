def dias_mes(mes, año):
    mes_con_30 = [4, 6, 9, 11]
    if mes == 2:
        if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
            return 29
        else:
            return 28
    elif mes in mes_con_30:
        return 30
    else:
        return 31
        

def calendario(fecha):
    dia_semana = ["lun", "mar", "mie", "jue", "vie", "sab", "dom"]
    fecha_referencia = datetime(fecha.year, fecha.month, 1)
    posicion = fecha_referencia.weekday()
    semana_1 = [1]
    while len(semana_1) != (posicion + 1):
        semana_1.insert(0, "")
    contador = 2
    while len(semana_1) != 7:
        semana_1.append(contador)
        contador += 1
    calendarios = [dia_semana, semana_1]
    semana = []
    while contador != dias_mes(fecha.month, fecha.year) + 1:
        if len(semana) == 7:
            calendarios.append(semana)
            semana = []
        semana.append(contador)
        contador += 1
    calendarios.append(semana)
    return calendarios

from datetime import datetime
cantidad = int(input())
for i in range(cantidad):
    fecha = datetime.strptime(input(), "%d/%m/%Y")
    calendarios = calendario(fecha)
    for i in calendarios:
        for j in range(len(i) - 1):
            print(i[j], end="\t")
        print(i[-1])
    print("")
