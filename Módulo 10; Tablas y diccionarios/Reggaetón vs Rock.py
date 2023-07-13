def palabras_distintas(cantidad):
    palabras = []
    for i in range(cantidad):
        renglon = input()
        renglon = renglon.split()
        for palabra in renglon:
            if palabra not in palabras:
                palabras.append(palabra)
    return len(palabras)

ren_reg = int(input())
cantidad_reg = palabras_distintas(ren_reg)
ren_roc = int(input())
cantidad_roc = palabras_distintas(ren_roc)
print("Reggaeton:", cantidad_reg, "Rock:", cantidad_roc)
