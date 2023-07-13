def f(x) :
    if x % 123 == 0:
        return 0
    return 1 + f(x + 23)

cantidad = int(input())
for i in range (cantidad) :
    valor = int(input())
    retorno = f(valor)
    print(retorno)
