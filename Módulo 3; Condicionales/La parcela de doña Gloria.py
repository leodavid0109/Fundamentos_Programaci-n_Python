lado_1 = float(input())
diagonal = float(input())
lado_2 = ((diagonal ** 2) - (lado_1 ** 2)) ** 0.5
area = lado_1 * lado_2
area_redondeada = round(area, 2)
print("El area total es de", area_redondeada, "metros cuadrados")
#De igual manera se puede escribir de la siguiente manera, es más cómodo.
print (f"El area total es de {area_redondeada} metros cuadrados")
