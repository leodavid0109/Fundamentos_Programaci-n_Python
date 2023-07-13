def suma_impar(lista) :
    suma = 0
    for i in range(1, len(lista), 2) :
        suma += lista[i]
    return suma

def promedio_par(lista) :
    suma = 0
    contador = 0
    for i in range(0, len(lista), 2) :
        suma += lista[i]
        contador += 1
    promedio = suma / contador
    resultado = round(promedio, 0) ** 8
    return int(resultado)

def multiplicacion_cifras(numero) :
    digitos = str(numero)
    multiplicacion = 1
    for i in range(len(digitos)) :
        multiplicacion *= int(digitos[i])
    return multiplicacion

def suma_cifras(numero) :
    digitos = str(numero)
    suma = 0
    for i in range(len(digitos)) :
        suma += int(digitos[i])
    return suma

def operacion(numero_1, numero_2) :
    resultado = (numero_1 * (numero_2 ** 3) + 5) / (4 + (numero_1 ** 2))
    redondeo = round(resultado, 0)
    return int(redondeo)

lista = []
numero = int(input())
while numero != 0 :
    lista.append(numero)
    numero = int(input())
final = operacion(multiplicacion_cifras(suma_impar(lista)), suma_cifras(promedio_par(lista)))
print(final)
