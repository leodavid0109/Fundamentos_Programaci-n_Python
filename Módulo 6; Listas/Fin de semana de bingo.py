identificador = int(input())
partidas = int(input())
registro = []
cantidad_triunfos = []
for i in range(partidas) :
    ganador = int(input())
    registro.append(ganador)
for j in range(identificador) :
    cantidad_triunfos.append(registro.count(j+1))
for k in range(identificador) :
    if max(cantidad_triunfos) == cantidad_triunfos[k] :
        print(k+1)
