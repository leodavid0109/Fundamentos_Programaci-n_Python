numero = int(input())
limite_inferior = int(input())
limite_superior = int(input())
valor_verdad = True
print(numero, end='')
for i in range (limite_inferior, limite_superior + 1) :
    if numero % i != 0 :
        valor_verdad = False
        break
    else :
        numero /= i
if valor_verdad == False :
    print(" no es polifactor entre", limite_inferior, "y", limite_superior)
else :
    print(" es polifactor entre", limite_inferior, "y", limite_superior)
