eleccion_1 = input()
eleccion_2 = input()
if eleccion_1 == eleccion_2 :
    print("empate")
elif ((eleccion_1 == "piedra") and (eleccion_2 == "tijera")) or ((eleccion_1 == "tijera") and (eleccion_2 == "papel")) or ((eleccion_1 == "papel") and (eleccion_2 == "piedra")) :
    print(eleccion_1, "vence", eleccion_2)
else :
    print(eleccion_2, "vence", eleccion_1)
