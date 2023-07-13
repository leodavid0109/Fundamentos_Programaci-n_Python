def bandera_escocia(dimension) :
    for j in range(1, dimension + 1) :
        for i in range(1, dimension + 1) :
            if i == j or i == dimension + 1 - j :
                print("#", end = "")
            else :
                print("0", end = "")
        print(end = "\n")

dimension = int(input())
while dimension != 0 :
    bandera_escocia(dimension)
    print("")
    dimension = int(input())
