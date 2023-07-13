largo = int(input())
alto = int(input())
i = 1
medio_largo = (largo + 1) / 2
medio_alto = (alto + 1) / 2
while i <= alto :
    if i != medio_alto :
        for j in range (1, largo + 1) :
            if j != medio_largo :
                print("0", end='')
            else :
                print("+", end='')
    else :
        for j in range (1, largo + 1) :
            print("+", end='')
    print(end='\n')
    i += 1
