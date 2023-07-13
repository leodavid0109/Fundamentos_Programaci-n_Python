from math import sqrt
def f(x) :
    f_evaluada = sqrt(2 + (5 * x))
    return f_evaluada

def g(x) :
    g_evaluada = (4 + x) ** 3
    return g_evaluada

valor_x = int(input())
while valor_x != 0 :
    if valor_x % 2 == 0 :
        compuesta_evaluada = f(g(valor_x))
        print(compuesta_evaluada)
    else :
        compuesta_evaluada = g(f(valor_x))
        print(compuesta_evaluada)
    valor_x = int(input())
