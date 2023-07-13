cantidad_partidos = int(input())
goles_barcelona = []
goles_real = []
puntos_barcelona = 0
puntos_real = 0
for i in range (cantidad_partidos) :
    gol_barca = int(input())
    goles_barcelona.append(gol_barca)
for j in range (cantidad_partidos) :
    gol_real = int(input())
    goles_real.append(gol_real)
for k in range (cantidad_partidos) :
    if goles_barcelona[k] > goles_real[k] :
        puntos_barcelona += 2
    elif goles_barcelona[k] < goles_real[k] :
        puntos_real += 2
    else :
        puntos_barcelona += 1
        puntos_real += 1
print("Ballenota Futbol Club:", puntos_barcelona)
print("Real Mandril:", puntos_real)
