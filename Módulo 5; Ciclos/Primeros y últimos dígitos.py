numero = int(input())
ultimo_digito = numero % 10
while numero >= 10 :
    numero //= 10
print(numero, ultimo_digito, sep='')
