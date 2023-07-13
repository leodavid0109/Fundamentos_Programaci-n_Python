cantidad_numeros = int(input())
numeros_vistos = []
for i in range (cantidad_numeros) :
    numero = int(input())
    numeros_vistos.append(numero)
for j in range (1, 6) :
    print(j, numeros_vistos.count(j), sep = ": ")
