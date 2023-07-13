def congruencia(dia, mes, año):
    meses = {"marzo":3, "abril":4, "mayo":5, "junio":6, "julio":7, "agosto":8, "septiembre":9, "octubre":10, "noviembre":11, "diciembre":12, "enero":13, "febrero":14}
    if mes == "enero" or mes == "febrero":
        año -= 1
    resultado = (dia + ((13 * (meses[mes] + 1))// 5) + año + (año // 4) - (año // 100) + (año // 400)) % 7
    return resultado

cantidad = int(input())
valores = {0:"sabado", 1:"domingo", 2:"lunes", 3:"martes", 4:"miercoles", 5:"jueves", 6:"viernes"}
for i in range(cantidad):
    fecha = input()
    fecha = fecha.split(sep = "-")
    residuo = congruencia(int(fecha[0]), fecha[1], int(fecha[2]))
    print(valores[residuo])
