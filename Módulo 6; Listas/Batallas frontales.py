soldados_bando = int(input())
bando_1 = []
bando_2 = []
sobrevivientes = 0
for i in range(soldados_bando) :
    estatura_1 = int(input())
    bando_1.append(estatura_1)
for j in range(soldados_bando) :
    estatura_2 = int(input())
    bando_2.append(estatura_2)
bando_1.sort()
bando_2.sort(reverse = True)
for k in range(soldados_bando) :
    if (bando_1[k] % 2) != (bando_2[k] % 2) :
        sobrevivientes += 2
print(f"Sobreviven {sobrevivientes} soldados")
