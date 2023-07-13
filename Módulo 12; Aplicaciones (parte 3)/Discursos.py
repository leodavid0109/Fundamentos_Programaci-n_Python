def limpieza(palabra):
    palabra = palabra.lower()
    palabra = palabra.rstrip("?")
    palabra = palabra.rstrip(".")
    palabra = palabra.rstrip(",")
    palabra = palabra.rstrip(":")
    palabra = palabra.rstrip(";")
    return palabra

texto = open("Discursos.txt", "r")
diccionario = {}
diccionarios = []
for renglon in texto:
    renglon = renglon.split()
    palabras = []
    for palabra in renglon:
        palabra = limpieza(palabra)
        if len(palabra) > 4:
            if palabra not in palabras:
                palabras.append(palabra)
    for i in palabras:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
            diccionarios.append(i)
diccionarios.sort()
for i in diccionarios:
    print(i, diccionario[i])
texto.close()
