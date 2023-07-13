numero = int(input())
if numero % 2 == 0 :
    print(numero, "es multiplo de 2")
elif numero % 3 == 0 :
    print(numero, "es multiplo de 3")
elif numero % 5 == 0 :
    print(numero, "es multiplo de 5")
elif numero % 7 == 0 :
    print(numero, "es multiplo de 7")
else :
    print(numero, "no es multiplo de ninguno de los primeros cuatro primos")
