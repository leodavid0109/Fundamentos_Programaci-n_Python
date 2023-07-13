capital = int(input())
retorno = int(input())
if retorno > capital :
    diferencia = retorno - capital
    variacion = (diferencia / capital) * 100
    print("Hubo una ganancia de $", diferencia, "correspondiente al", variacion, "% del capital invertido")
elif capital > retorno :
    diferencia = capital - retorno
    variacion = (diferencia / capital) * 100
    print("Hubo una perdida de $", diferencia, "correspondiente al", variacion, "% del capital invertido")
else :
    print("No hubo ni ganancia ni perdida, la inversion fue un desperdicio de tiempo, pero al menos no de dinero")
