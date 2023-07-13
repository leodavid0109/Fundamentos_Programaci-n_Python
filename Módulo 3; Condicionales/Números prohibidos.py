numero_calle = int(input())
numero_casa = int(input())
if ((numero_calle % 13 == 0) or (numero_calle % 23 == 0)) or ((numero_casa % 13 == 0) or (numero_casa % 23 == 0)) :
    print ("La direccion calle", numero_calle, "#", numero_casa, "esta prohibida")
else :
    print ("La direccion calle", numero_calle, "#", numero_casa, "no esta prohibida")
