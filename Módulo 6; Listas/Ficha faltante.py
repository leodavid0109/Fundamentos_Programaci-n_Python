cantidad_fichas = int(input())
fichas = []
for i in range (cantidad_fichas - 1) :
    ficha = int(input())
    fichas.append(ficha)
for j in range(1, cantidad_fichas + 1) :
    if j not in fichas :
        print("La ficha faltante es la", j)
        break
