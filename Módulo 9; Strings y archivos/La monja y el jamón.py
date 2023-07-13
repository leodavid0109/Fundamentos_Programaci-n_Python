def trifelio(palabra) :
    palabra = palabra.split("-")
    p = palabra[1]
    p = p.replace("\n","")
    palabra.pop()
    palabra.append(p)
    palabra_1 = palabra[0]
    letra = len(palabra_1)
    x = 1
    palabra_2 = palabra_1
    while x < letra :
        word = palabra_2[0]
        palabra_2 = palabra_2[1:]
        palabra_2 += word
        if palabra_2 == palabra[1] :
            return True
        x += 1
    return False

texto = open("La monja y el jamón.txt", "r")
for renglon in texto :
    if trifelio(renglon) :
        print("Es trifelio")
    else :
        print("No es trifelio")
texto.close()
