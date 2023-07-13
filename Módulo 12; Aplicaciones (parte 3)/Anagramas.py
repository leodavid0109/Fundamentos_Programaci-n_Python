def anagrama(palabra_1, palabra_2):
    letras_1 = {}
    letras_2 = {}
    for letra in palabra_1:
        if letra in letras_1:
            letras_1[letra] += 1
        else:
            letras_1[letra] = 1
    for letra in palabra_2:
        if letra in letras_2:
            letras_2[letra] += 1
        else:
            letras_2[letra] = 1
    if letras_1 == letras_2:
        return True
    return False

cantidad = int(input())
for i in range(cantidad):
    caso = input()
    caso = caso.split(" : ")
    palabra_1 = ""
    palabra_2 = ""
    caso_1 = caso[0].split()
    for i in caso_1:
        palabra_1 += i
    caso_2 = caso[1].split()
    for i in caso_2:
        palabra_2 += i
        
    if anagrama(palabra_1, palabra_2):
        print("Es anagrama")
    else:
        print("No es anagrama")
