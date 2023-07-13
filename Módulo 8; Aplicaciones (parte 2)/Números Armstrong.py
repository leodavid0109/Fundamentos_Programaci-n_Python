def numero_armstrong(numero) :
    entero = str(numero)
    digitos = len(entero)
    suma = 0
    for i in range(digitos) :
        suma += (int(entero[i]) ** digitos)
    if numero == suma :
        return True
    return False

cantidad = int(input())
for i in range(cantidad) :
    numero = int(input())
    if numero_armstrong(numero) :
        print(numero, "es Armstrong")
    else :
        print(numero, "no es Armstrong")
