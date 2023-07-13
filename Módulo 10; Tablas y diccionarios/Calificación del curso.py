def nota_final(correctos, totales):
    nota_taller = []
    cont = 0
    for i in range(12):
        nota = (correctos[i] / totales[i]) * 5
        nota = round(nota, 1)
        nota_taller.append(nota)
        cont += nota
    final = cont / 12
    final = round(final, 1)
    return final

cantidad = int(input())
puntos_taller = [9, 11, 12, 8, 12, 9, 11, 8, 11, 10, 9, 10]
lista = []
for i in range(cantidad):
    datos = input()
    lista.append(datos)
final = []
for renglon in lista:
    renglon = renglon.split(sep = ", ")
    for i in range(len(renglon)):
        renglon[i] = int(renglon[i])
    ID = renglon.pop(0)
    final.append([ID, nota_final(renglon, puntos_taller)])
final.sort()
for i in final:
    print(i[0], i[1])
