cantidad_kilometros = int(input("Digite la cantidad de kilómetros que recorrió con el vehículo:"))
monto_fijo = 300000
iva = 0.20
if cantidad_kilometros <= 300 :
    monto_final = monto_fijo
elif cantidad_kilometros <= 1000 :
    monto_final = monto_fijo + (15000 * (cantidad_kilometros - 300))
else :
    monto_final = monto_fijo + (15000 * 700) + (10000 * (cantidad_kilometros - 1000))
monto_iva = iva * monto_final
print ("El valor total a pagar es:", monto_final, ", de lo cual,", monto_iva, "corresponde a impuestos sobre la compra.")
