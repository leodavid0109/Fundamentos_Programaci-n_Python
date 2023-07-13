def cadena(frase) :
    frase = frase.split()
    for i in range(len(frase) - 1) :
        palabra_1 = frase[i]
        palabra_2 = frase[i + 1]
        if (palabra_1[-2] == palabra_2[0] and palabra_1[-1] == palabra_2[1]) or (palabra_1[-3] == palabra_2[0] and palabra_1[-2] == palabra_2[1] and palabra_1[-1] == palabra_2[2]) :
            continue
        else :
            return False
    return True

texto = open("Cadena de palabras.txt", "r")
for renglon in texto :
    if cadena(renglon) :
        print("cadena completa")
    else :
        print("cadena rota")
texto.close()
