cantidad_lotes = int(input())
longitud = float(input())
incremento = float(input())
area = 0
for i in range (1, cantidad_lotes+1):
    area += longitud**2
    longitud += incremento
print("El area total es de", area, "metros cuadrados")
