porcentaje = float(input())
if porcentaje < 40 :
    calificacion = "F"
elif porcentaje < 60 :
    calificacion = "E"
elif porcentaje < 70 :
    calificacion = "D"
elif porcentaje < 80 :
    calificacion = "C"
elif porcentaje < 90 :
    calificacion = "B"
else :
    calificacion = "A"
print("El porcentaje", porcentaje, "corresponde a la calificacion", calificacion)
