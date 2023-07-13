def enchufar(cables) :
    hembra = cables.count("F")
    macho = cables.count("M")
    if hembra == macho :
        return True
    return False

cantidad = int(input())
for i in range(cantidad) :
    cables = input()
    if enchufar(cables) :
        print("Es posible hacer un unico circulo")
    else :
        print("No es posible")
