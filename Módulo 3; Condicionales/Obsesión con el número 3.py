numero = int(input())
if numero == 3 :
    print("El numero 3 es el mejor")
elif numero % 3 == 0 :
    print("El numero", numero, "es multiplo de 3. Y el numero 3 es el mejor")
elif (numero - 1) % 3 == 0 :
    print("El numero", numero, "no es multiplo de 3, pero si le restas 1 el resultado si lo es. Y el numero 3 es el mejor")
else :
    print("El numero", numero, "no es multiplo de 3, pero si le sumas 1 el resultado si lo es. Y el numero 3 es el mejor")
