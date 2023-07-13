num1 = int(input("Digite un número: "))
if num1%2==0 :
    print ("El número", num1, "es par.")
elif num1%3==0 :
    print ("El número", num1, "es divisible por 3.")
elif num1%5==0 and num1%7==0 :
    print ("El número", num1, "es divisible por 5 y por 7")
else :
    print ("El número", num1, "es complejo")
