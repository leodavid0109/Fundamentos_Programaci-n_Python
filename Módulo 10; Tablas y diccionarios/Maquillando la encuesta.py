cantidad = int(input())
lista = []
for i in range(cantidad):
    datos = input()
    datos = datos.split()
    if datos[2] == "positiva" :
        lista.append(datos)
for j in range(len(lista)):
    lista[j][3] = int(lista[j][3])
lista.sort(key = lambda x: x[1], reverse = True)
lista.sort(key = lambda x: x[3], reverse = True)
for renglon in lista:
    opinion = renglon[2]
    print(renglon[1], opinion.upper(), renglon[3])
