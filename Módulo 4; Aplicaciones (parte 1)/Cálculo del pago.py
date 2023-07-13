tarifa = int(input())
cantidad_horas = int(input())
pago = cantidad_horas * tarifa
if cantidad_horas > 45 :
    pago_1 = (cantidad_horas - 45) * (tarifa * 0.5)
    pago = pago + pago_1
print("$", int(pago))
