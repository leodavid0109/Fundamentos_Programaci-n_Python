segundos = int(input())
minutos = segundos // 60
segundos = segundos % 60
horas = minutos // 60
minutos = minutos % 60
print(horas, minutos, segundos, sep=":")
