def poker(numeros, palo) :
    numeros.sort()
    mismo_palo = True
    consecutivas = True
    for k in range(len(palo) - 1) :
        if palo[k] != palo[k+1] :
            mismo_palo = False
            break
    for l in range(len(palo) - 1) :
        if (numeros[l+1] - numeros[l]) != 1 :
            consecutivas = False
            break
    if mismo_palo and consecutivas :
        if numeros[0] == 10 :
            print("Escalera real")
        else :
            print("Escalera de color")
    elif mismo_palo :
        print("Color")
    elif consecutivas :
        print("Escalera normal")
    else :
        print("Otra mano")

cantidad = int(input())
for i in range(cantidad) :
    numeros = []
    palo = []
    for j in range(5) :
        valor = int(input())
        tipo = input()
        numeros.append(valor)
        palo.append(tipo)
    poker(numeros, palo)
