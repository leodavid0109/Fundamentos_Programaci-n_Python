salarios = []
sueldo = int(input())
while sueldo != 0 :
    salarios.append(sueldo)
    sueldo = int(input())
salarios.sort()
indice = (salarios[-3] - salarios[2]) / (len(salarios) ** 2)
indice_1 = round(indice, 2)
print(indice_1)
