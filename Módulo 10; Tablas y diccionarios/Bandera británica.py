def bandera(dimension):
    dibujo = []
    for i in range(dimension):
        linea = input()
        dibujo.append(linea)
    for j in range(dimension):
        for k in range(dimension):
            if k == j or k == dimension - 1 - j:
                if dibujo[j][k] != "#":
                    return "Ni idea"
            elif j == ((dimension - 1) / 2) or k == ((dimension - 1) / 2):
                if dibujo[j][k] != "+":
                    return "Ni idea"
            elif dibujo[j][k] != "0":
                return "Ni idea"
    return "Bandera britanica"

cantidad = int(input())
for i in range(cantidad):
    dimension = int(input())
    print(bandera(dimension))
