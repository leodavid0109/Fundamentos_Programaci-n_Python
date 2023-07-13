pasajero = int(input())
parejas = []
contador = 0
while pasajero != 0 :
    parejas.append(pasajero)
    pasajero = int(input())
for i in range(len(parejas)) :
    for j in range(i, len(parejas)) :
        if (parejas[i] + parejas[j]) == 1995 :
            contador += 1
print(contador)
