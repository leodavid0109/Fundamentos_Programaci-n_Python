def encripcion(archivo) :
    renglones = []
    for renglon in archivo :
        if "\n" in renglon :
            renglones.append(renglon[-2::-1])
        else :
            renglones.append(renglon[::-1])
    return renglones

archivo = open("Mensaje encriptado.txt", "r")
renglones = encripcion(archivo)
for i in renglones :
    print(i)        
archivo.close()
