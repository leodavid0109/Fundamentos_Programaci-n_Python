retiro = int(input())
retiro_50 = retiro // 50000
residuo_1 = retiro % 50000
retiro_20 = residuo_1 // 20000
residuo_2 = residuo_1 % 20000
retiro_10 = residuo_2 // 10000
residuo_3 = residuo_2 % 10000
retiro_5 = residuo_3 // 5000
residuo_4 = residuo_3 % 5000
retiro_2 = residuo_4 // 2000
residuo_5 = residuo_4 % 2000
retiro_1 = residuo_5 // 1000
if retiro_50 != 0 :
    print (retiro_50, "de $50000")
if retiro_20 != 0 :
    print (retiro_20, "de $20000")
if retiro_10 != 0 :
    print (retiro_10, "de $10000")
if retiro_5 != 0 :
    print (retiro_5, "de $5000")
if retiro_2 != 0 :
    print (retiro_2, "de $2000")
if retiro_1 != 0 :
    print (retiro_1, "de $1000")
