hora = int(input())
minuto = int(input())
minuto_final = 60 - minuto
if minuto_final == 60 :
    minuto_final = 0
if minuto == 0 :
    hora_final = 12 - hora
else :
    hora_final = (12 - hora) - 1
if hora_final == 0 :
    hora_final = 12
elif hora_final == -1 :
    hora_final = 11
print(hora_final,minuto_final, sep=":")
