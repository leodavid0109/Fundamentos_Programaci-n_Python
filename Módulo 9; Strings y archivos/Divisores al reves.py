def divisores_reves(numero) :
    divisores = []
    for i in range(1, numero + 1) :
        if numero % i == 0 :
            divisores.append(i)
    print(divisores)
    for j in divisores :
        print(str(j)[::-1])

numero = int(input())
divisores_reves(numero)
