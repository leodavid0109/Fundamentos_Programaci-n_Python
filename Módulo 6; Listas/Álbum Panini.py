cromos_distintos = []
cromo = int(input())
while cromo != 0 :
    if cromo not in cromos_distintos :
        cromos_distintos.append(cromo)
    cromo = int(input())
print(len(cromos_distintos))
