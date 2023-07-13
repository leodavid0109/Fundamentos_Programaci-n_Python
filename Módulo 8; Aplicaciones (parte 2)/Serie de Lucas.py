def serie_lucas(limite) :
    serie = [2, 1]
    while serie[-1] <= limite :
        numero = serie[-1] + serie[-2]
        serie.append(numero)
    return serie

valor_inicial = int(input())
valor_final = int(input())
lista = serie_lucas(valor_final)
cantidad = 0
for i in range(valor_inicial, valor_final + 1) :
    if i in lista :
        cantidad += 1
print(cantidad)
