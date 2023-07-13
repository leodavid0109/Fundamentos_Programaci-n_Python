def traspuesta(matriz):
    tras = []
    for i in range(len(matriz)):
        columna = []
        for j in range(len(matriz)):
            columna.append(matriz[j][i])
        tras.append(columna)
    return tras

matriz = [[1,2,3],[1,2,3],[1,2,3]]
tras = traspuesta(matriz)
tras_1 = traspuesta(tras)
print(tras)
print(tras_1)
