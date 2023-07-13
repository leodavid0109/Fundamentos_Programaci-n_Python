def procedencia(palabra) :
    if palabra[-2] == "i" and palabra[-1] == "x" :
        return("Galo")
    elif palabra[-2] == "u" and palabra[-1] == "s" :
        return("Romano")
    elif palabra[-2] == "i" and palabra[-1] == "c" :
        return("Godo")
    elif palabra[-2] == "a" and palabra[-1] == "s" :
        return("Griego")
    elif palabra[-2] == "a" and palabra[-1] == "f" :
        return("Normando")
    elif (palabra[-2] == "i" and palabra[-1] == "s") or (palabra[-2] == "a" and palabra[-1] == "x") :
        return("Breton")
    elif palabra[-2] == "e" and palabra[-1] == "z" :
        return("Hispano")
    elif palabra[-1] == "a":
        return("Indio")
    else :
        return("Desconocido")

cantidad = int(input())
for i in range(cantidad) :
    palabra = input()
    print(procedencia(palabra))
