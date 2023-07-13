coordenada_x = float(input())
coordenada_y = float(input())
if coordenada_x == 0 and coordenada_y == 0 :
    print(f"La coordenada ({coordenada_x}, {coordenada_y}) corresponde al origen")
elif coordenada_x == 0 or coordenada_y == 0 :
    if coordenada_x == 0 :
        print(f"La coordenada ({coordenada_x}, {coordenada_y}) esta sobre el eje Y")
    else :
        print(f"La coordenada ({coordenada_x}, {coordenada_y}) esta sobre el eje X")
elif coordenada_x > 0 :
    if coordenada_y > 0 :
        print(f"La coordenada ({coordenada_x}, {coordenada_y}) se encuentra en el cuadrante 1")
    else :
        print(f"La coordenada ({coordenada_x}, {coordenada_y}) se encuentra en el cuadrante 4")
else :
    if coordenada_y > 0 :
        print(f"La coordenada ({coordenada_x}, {coordenada_y}) se encuentra en el cuadrante 2")
    else :
        print(f"La coordenada ({coordenada_x}, {coordenada_y}) se encuentra en el cuadrante 3")
