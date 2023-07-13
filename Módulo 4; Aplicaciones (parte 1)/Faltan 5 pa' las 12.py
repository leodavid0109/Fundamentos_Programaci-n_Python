horas = int(input())
minutos = int(input())
parte_dia = input()
minuto_minutos = 0
if horas == 12 and minutos == 0 and parte_dia == "am" :
    print("Faltan 1440 para las 12")
elif horas == 12 and minutos == 0 and parte_dia == "pm" :
    print("Faltan 720 para las 12")
elif horas == 12 and parte_dia == "am" :
    minuto_final = (60 - minutos) + (23 * 60)
    print("Faltan", minuto_final, "para las 12")
elif horas == 12 and parte_dia == "pm" :
    minuto_final = (60 - minutos) + (11 * 60)
    print("Faltan", minuto_final, "para las 12")
else :
    if minutos == 0 :
        hora_restante = 12 - horas
        minuto_hora = hora_restante * 60
    else :
        hora_restante = 11 - horas
        minuto_hora = hora_restante * 60
        minuto_minutos = 60 - minutos
    minuto_final = minuto_hora + minuto_minutos
    if parte_dia == "am" :
        minuto_final = minuto_final + (12 * 60)
    print("Faltan", minuto_final, "para las 12")
