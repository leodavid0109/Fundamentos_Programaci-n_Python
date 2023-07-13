def punto_espejo(lista) :
    cantidad = 0
    for i in range(1, len(lista)) :
        suma_izquierda = 0
        suma_derecha = 0
        for j in range(i-1, -1, -1) :
            suma_izquierda += lista[j]
        for k in range(i, len(lista)) :
            suma_derecha += lista[k]
        if suma_izquierda == suma_derecha :
            cantidad += 1
    return cantidad

cantidad_valores = int(input())
lista = []
for x in range(cantidad_valores) :
    valor = float(input())
    lista.append(valor)
cantidad = punto_espejo(lista)
print(cantidad)
