def multidigito(numero) :
    digitos = str(numero)
    for i in range(1,6) :
        if str(i) not in digitos :
            return False
    return True

numero = int(input())
while numero != 0 :
    if multidigito(numero) :
        print("Multidigito")
    else :
        print("No es multidigito")
    numero = int(input())
