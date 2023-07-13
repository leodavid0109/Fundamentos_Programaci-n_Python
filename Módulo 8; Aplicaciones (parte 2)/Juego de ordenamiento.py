def ordenamiento(lista) :
    orden = []
    ordenada = sorted(lista)
    for j in range(len(lista)) :
        for i in range(len(lista)) :
            if lista[i] == ordenada[j] :
                orden.append(i+1)
                break
    return orden

cantidad = int(input())
numeros = []
for i in range(cantidad) :
    valor = float(input())
    numeros.append(valor)
orden = ordenamiento(numeros)
for j in orden :
    print(j)
