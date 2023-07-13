valor_compra = int(input())
valor_efectivo = int(input())
vueltos = valor_efectivo - valor_compra
print (vueltos)
if ((vueltos % 10 == 0) or (vueltos % 15 == 0)) and (vueltos % 4 != 0) :
    print ("y te lo puedes quedar")
