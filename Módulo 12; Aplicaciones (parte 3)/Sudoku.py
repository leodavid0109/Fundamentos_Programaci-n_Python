def resuelto(propuesta):
    for i in range(9):
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            if propuesta[i][j] not in numeros:
                return False
            numeros.remove(propuesta[i][j])
    for i in range(9):
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            if propuesta[j][i] not in numeros:
                return False
            numeros.remove(propuesta[j][i])
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for k in range(i, i+3):
                numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for l in range(j, j+3):
                    if propuesta[k][l] not in numeros:
                        return False
                    numeros.remove(propuesta[k][l])
    return True

cantidad = int(input())
for i in range(cantidad):
    caso = input()
    propuesta = []
    for i in range(9):
        fila = input()
        fila = fila.split()
        for i in range(9):
            fila[i] = int(fila[i])
        propuesta.append(fila)
    if resuelto(propuesta):
        print("Resuelto")
    else:
        print("No resuelto")
