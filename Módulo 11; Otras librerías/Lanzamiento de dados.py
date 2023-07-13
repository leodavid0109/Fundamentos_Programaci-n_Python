def ganador(plataforma, humano):
    if plataforma > humano:
        print("Gana la plataforma")
    elif plataforma < humano:
        print("Gana el humano")
    else:
        print("Empate")

from random import randint
cantidad = int(input())
for i in range(cantidad):
    lanzamiento = input()
    lanzamiento = lanzamiento.split()
    plataforma = int(lanzamiento[1])
    humano = randint(1, 6) + randint(1, 6)
    ganador(plataforma, humano)
