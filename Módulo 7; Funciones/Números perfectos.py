def numero_perfecto(valor) :
    suma = 0
    for i in range (valor - 1, 0, -1) :
        if valor % i == 0 :
            suma += i
    if suma != valor:
        return False
    return True

cantidad = int(input())
for i in range(cantidad) :
    valor = int(input())
    if numero_perfecto(valor) :
        print(valor, "es perfecto")
    else :
        print(valor, "no es perfecto")
