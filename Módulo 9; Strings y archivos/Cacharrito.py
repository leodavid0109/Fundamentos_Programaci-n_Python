def ordenador_placas(placas) :
    placas = placas.split()
    placa = placas[0]
    placas.sort()
    if placa == placas[0] :
        return True
    return False

cantidad = int(input())
for i in range(cantidad) :
    placas = input()
    if ordenador_placas(placas) :
        print("Mi cacharrito es el mas viejo de todos los autos ;D")
    else :
        print("Al menos otro auto es mas viejo que mi cacharrito :(")
