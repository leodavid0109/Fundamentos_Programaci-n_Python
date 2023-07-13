cantidad_uvas = int(input())
racimos_ideales = [1]
while cantidad_uvas != 0 :
    while racimos_ideales[-1] < cantidad_uvas :
        nivel = racimos_ideales[-1] + (len(racimos_ideales)+1)
        racimos_ideales.append(nivel)
    if cantidad_uvas in racimos_ideales :
        print("Puede ser un racimo ideal")
    else :
        print("No puede ser un racimo ideal")
    cantidad_uvas = int(input())
