from math import sqrt
velocidad_luz = 299792458
def conversor(velocidad) :
    velocidad *= (10 / 36)
    return(velocidad)

def factor_lorentz(velocidad) :
    factor = 1 / sqrt(1 - ((velocidad ** 2) / (velocidad_luz ** 2)))
    return factor

cantidad_valores = int(input())
for i in range (cantidad_valores) :
    velocidad_evaluar = float(input())
    conversion = conversor(velocidad_evaluar)
    factor_calculado = factor_lorentz(conversion)
    print(round(factor_calculado, 15))
