def hyperpar(numero) :
    unidades = str(numero)
    if numero % 2 == 0 :
        for i in range (len(unidades)) :
            if int(unidades[i]) % 2 != 0 :
                return False
        return True

numero = int(input())
while numero != -1 :
    if hyperpar(numero) :
        print("Hyperpar")
    else :
        print("No es hyperpar")
    numero = int(input())
