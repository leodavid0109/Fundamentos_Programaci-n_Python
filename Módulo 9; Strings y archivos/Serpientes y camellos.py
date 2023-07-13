def serpiente_camello(palabra) :
    palabra = palabra.split("_")
    for i in range(len(palabra)) :
        palabra[i] = palabra[i].capitalize()
    return palabra

cantidad = int(input())
for i in range(cantidad) :
    palabra = input()
    frase_camello = serpiente_camello(palabra)
    frase = ""
    for i in frase_camello :
        frase += i
    print(frase)
