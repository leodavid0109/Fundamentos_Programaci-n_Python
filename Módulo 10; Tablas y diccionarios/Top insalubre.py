def IMC(peso, estatura):
    indice = peso / (estatura ** 2)
    indice = round(indice, 1)
    return indice

cantidad = int(input())
lista = []
for i in range(cantidad):
    datos = input()
    datos = datos.split(sep = ", ")
    for j in range(1, len(datos)):
        datos[j] = float(datos[j])
    lista.append(datos)
final = []
for renglon in lista:
    if renglon[3] > 100 and renglon[4] > 150:
        indice = IMC(renglon[1], renglon[2])
        if indice > 25:
            final.append([renglon[0], indice])
final.sort(key = lambda x: x[0], reverse = True)
final.sort(key = lambda x: x[1], reverse = True)
for i in range(len(final)):
    print(i + 1, final[i][0], final[i][1])
