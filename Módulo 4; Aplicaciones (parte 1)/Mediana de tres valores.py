valor_1 = float(input())
valor_2 = float(input())
valor_3 = float(input())
if ((valor_2 <= valor_1) and (valor_1 <= valor_3)) or ((valor_3 <= valor_1) and (valor_1 <= valor_2)) :
    print(valor_1, "es la mediana")
elif ((valor_1 <= valor_2) and (valor_2 <= valor_3)) or ((valor_3 <= valor_2) and (valor_2 <= valor_1)) :
    print(valor_2, "es la mediana")
else :
    print(valor_3, "es la mediana")
