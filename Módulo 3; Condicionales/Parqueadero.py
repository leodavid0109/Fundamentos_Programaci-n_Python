tiempo_hora = int(input("Digite la cantidad de horas que duro estacionado: "))
tiempo_minutos = int(input("Digite la cantidad de minutos que duro estacionado: "))
if tiempo_minutos>0 :
    valor_pago = 2500 * (tiempo_hora + 1)
    print ("El valor total a pagar es:", valor_pago)
else :
    valor_pago = 2500 * tiempo_hora
    print ("El valor total a pagar es:", valor_pago)

#Como algoritmo alternativo, podemos sacar el valor de pago hacia afuera, definiendo
    #solamente el tiempo total dentro de la condición y haciendo por aparte el valor total.
