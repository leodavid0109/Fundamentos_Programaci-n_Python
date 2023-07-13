cantidad = int(input())
diccionario = {"true vampires":0, "early birds":0, "sunny warmers":0, "lunch workers":0, "sunset lovers":0, "prime timers":0}
commits = []
for i in range(cantidad):
    caso = input()
    caso = caso.split()
    caso[1] = caso[1].split(":")
    commits.append(caso[1])
for i in commits:
    i[0] = int(i[0])
for i in commits:
    if i[0] >= 0 and i[0] < 4:
        diccionario["true vampires"] += 1
    elif i[0] < 8:
        diccionario["early birds"] += 1
    elif i[0] < 12:
        diccionario["sunny warmers"] += 1
    elif i[0] < 16:
        diccionario["lunch workers"] += 1
    elif i[0] < 20:
        diccionario["sunset lovers"] += 1
    else:
        diccionario["prime timers"] += 1
for i in diccionario:
    print(i, diccionario[i])
