def triangular_superior(matriz):
    for i in range(1, len(matriz)):
        for j in range(i):
            if matriz[i][j] != 0:
                return False
    for i in range(len(matriz)-1):
        for j in range(i+1, len(matriz)):
            if matriz[i][j] != 0:
                return True
    return False

def triangular_inferior(matriz):
    for i in range(len(matriz)-1):
        for j in range(i+1, len(matriz)):
            if matriz[i][j] != 0:
                return False
    for i in range(1, len(matriz)):
        for j in range(i):
            if matriz[i][j] != 0:
                return True
    return False

def diagonal(matriz):
    for i in range(1, len(matriz)):
        for j in range(i):
            if matriz[i][j] != 0:
                return False
    for i in range(len(matriz)-1):
        for j in range(i+1, len(matriz)):
            if matriz[i][j] != 0:
                return False
    return True

cantidad = int(input())
for i in range(cantidad):
    longitud = int(input())
    matriz = []
    for i in range(longitud):
        fila = input()
        fila = fila.split()
        for j in range(len(fila)):
            fila[j] = float(fila[j])
        matriz.append(fila)
    if triangular_superior(matriz):
        print("Triangular superior")
    elif triangular_inferior(matriz):
        print("Triangular inferior")
    elif diagonal(matriz):
        print("Diagonal")
    else:
        print("Ni diagonal ni triangular")
