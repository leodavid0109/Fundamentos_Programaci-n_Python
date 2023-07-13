cantidad = int(input())
vendedores = {}
for i in range(cantidad):
    mensaje = input()
    mensaje = mensaje.split(sep = ": ")
    if vendedores == {}:
        primero = mensaje[0]
    if mensaje[0] not in vendedores:
        vendedores[mensaje[0]] = int(mensaje[1])
    else :
        vendedores[mensaje[0]] += int(mensaje[1])
maximo = [primero, vendedores[primero]]
for i in vendedores:
    if vendedores[i] > maximo[1]:
        maximo[0] = i
        maximo[1] = vendedores[i]
print("El vendedor del mes es", maximo[0])
