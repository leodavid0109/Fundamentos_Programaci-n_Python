def serie_julianachi(numero) :
    def divisores(num) :
        divisor = [1]
        for i in range(2, num + 1) :
            if num % i == 0 :
                divisor.append(i)
        return divisor

    serie = [1]
    while serie[-1] <= numero :
        valor = serie[-1] + len(divisores(serie[-1]))
        serie.append(valor)
    return serie

numero = int(input())
serie = serie_julianachi(5000)
while numero != 0 :
    if numero in serie :
        print("Pertenece a la serie de Julianachi")
    else :
        print("No pertenece a la serie de Julianachi")
    numero = int(input())
