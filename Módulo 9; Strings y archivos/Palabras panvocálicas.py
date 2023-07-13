def panvocalica(palabra) :
    vocales = ["a", "e", "i", "o", "u"]
    for i in vocales :
        if i not in palabra :
            return False
    return True

cantidad = int(input())
for i in range(cantidad) :
    palabra = input()
    if panvocalica(palabra) :
        print("Panvocalica")
    else :
        print("No es panvocalica")
