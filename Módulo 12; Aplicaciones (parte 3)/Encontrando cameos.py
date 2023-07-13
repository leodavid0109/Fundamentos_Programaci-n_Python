def cameos(texto):
    cameo = "saramago"
    texto = texto.lower()
    contador = 0
    while texto != "":
        if cameo == "":
            contador += 1
            cameo = "saramago"
        if cameo[0] == texto[0]:
            cameo = cameo[1:]
        texto = texto[1:]
    return contador

texto = open("Cameos.txt", "r")
for renglon in texto:
    cantidad_cameos = cameos(renglon)
    print(cantidad_cameos)
texto.close()
