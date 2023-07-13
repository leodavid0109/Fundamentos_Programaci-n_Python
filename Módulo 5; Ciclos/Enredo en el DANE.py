dias = int(input())
total_nacimientos = 0
for i in range (1, dias+1) :
    promedio = float(input())
    nacimientos = (promedio * i) - total_nacimientos
    total_nacimientos += nacimientos
    print(int(nacimientos))
