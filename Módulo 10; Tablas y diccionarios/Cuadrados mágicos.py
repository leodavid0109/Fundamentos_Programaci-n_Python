def cuad(cuadrado):
    suma = 0
    for j in range(4):
        suma += cuadrado[0][j]
    for j in range(1, 4):
        suma_2 = 0
        for k in range(4):
            suma_2 += cuadrado[j][k]
        if suma_2 != suma:
            return False
    for j in range(4):
        suma_3 = 0
        for k in range(4):
            suma_3 += cuadrado[k][j]
        if suma_3 != suma:
            return False
    suma_4 = 0
    for j in range(4):
        suma_4 += cuadrado[j][j]
    if suma_4 != suma:
        return False
    suma_5 = 0
    for j in range(-1, -5, -1):
        suma_5 += cuadrado[j][j]
    if suma_5 != suma:
        return False
    return True
        
cantidad = int(input())
for i in range(cantidad):
    cuadrado = []
    caso = input()
    for j in range(4):
        valores = input()
        valores = valores.split()
        for k in range(4):
            valores[k] = int(valores[k])
        cuadrado.append(valores)
    if cuad(cuadrado):
        print("Cuadrado magico")
    else:
        print("Cuadrado muggle")
