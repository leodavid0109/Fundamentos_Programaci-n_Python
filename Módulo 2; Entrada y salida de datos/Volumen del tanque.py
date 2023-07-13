from math import pi
radio = float(input())
altura = float(input())
tasa = float(input())
minutos = float(input())
volumen = pi * (radio ** 2) * altura
cantidad_vaciada = tasa * minutos
if cantidad_vaciada >= volumen :
    volumen_final = 0
    print(volumen_final)
else :
    volumen_final = volumen - cantidad_vaciada
    final_redondeado = round(volumen_final, 3)
    print(final_redondeado)
