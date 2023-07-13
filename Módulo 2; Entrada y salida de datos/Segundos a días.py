s = int(input("Ingrese el valor en segundos que desea convertir: "))
m = s//60 #División entera me dan segundos.
s = s%60
h = m//60
m = m%60
d = h//24
h = h%24
print(d, "días,", h, "horas,", m, "minutos y", s, "segundos")
