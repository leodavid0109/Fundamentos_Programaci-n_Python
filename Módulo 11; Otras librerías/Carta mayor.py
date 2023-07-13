def generador_caso():
    from random import sample
    cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4
    eleccion = sample(cartas, k = 10)
    return eleccion

def juego(humano, plataforma):
    punto_h = 0
    punto_p = 0
    for i in range(10):
        if humano[i] > plataforma[i]:
            punto_h += 1
        elif humano[i] < plataforma[i]:
            punto_p += 1
    return punto_h, punto_p

cantidad = int(input())
for i in range(cantidad):
    humano = generador_caso()
    plataforma = []
    caso = input()
    caso = caso.split()
    for i in range(1, len(caso)):
        caso[i] = int(caso[i])
        plataforma.append(caso[i])
    punto_h, punto_p = juego(humano, plataforma)
    print("Puntos humano:", punto_h, "Puntos plataforma:", punto_p)
