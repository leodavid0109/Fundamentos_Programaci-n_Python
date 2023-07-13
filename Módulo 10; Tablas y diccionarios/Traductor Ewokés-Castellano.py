palabras = int(input())
diccionario = {}
for i in range(palabras):
    vocabulario = input()
    vocabulario = vocabulario.split()
    diccionario[vocabulario[0]] = vocabulario[1]
traducciones = int(input())
for i in range(traducciones):
    palabra = input()
    if palabra in diccionario:
        print(diccionario[palabra])
    else:
        print("palabra no encontrada")
