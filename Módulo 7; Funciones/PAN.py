def P(x) :
    return (2 * x) + 1

def A(x) :
    return 3 ** x

def N(x) :
    from math import sqrt
    return sqrt((5 * x) + 4)

cantidad = int(input())
for i in range(cantidad) :
    valor = float(input())
    retorno = P(A(N(valor)))
    print(retorno)
