def factorial(numero) :
    if numero == 0 :
        return 1
    return numero * factorial(numero - 1)

def numero_fuerte(numero) :
    digitos = str(numero)
    suma = 0
    for i in range(len(digitos)) :
        suma += factorial(int(digitos[i]))
    if suma == numero :
        return True
    return False

cantidad = int(input())
for i in range(cantidad) :
    valor = int(input())
    if numero_fuerte(valor) :
        print(valor, "es fuerte")
    else :
        print(valor, "no es fuerte")
