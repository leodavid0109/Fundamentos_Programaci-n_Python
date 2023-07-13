print ("Bienvenido, este programa consta de un convertidor de centímetros a pulgadas y en viceversa.")
print ("Sin más preámbulo, iniciemos.")
print ("Elija con el numeral de la opción, el proceso que desea realizar")
print ("1. Centímetros a pulgadas.")
print ("2. Pulgadas a centímetros.")
opcion = input()
if opcion == "1" :
    print ("Genial")
    cen = float(input("Digite el valor que desea convertir: "))
    pul = cen/2.54
    print ("El valor de", cen, "en pulgadas es", pul)
    
