def pregunta(renglon):
    preguntas = []
    creacion = ""
    for i in range(len(renglon)):
        if "?" not in renglon[0]:
            renglon.pop(0)
    while renglon != []:
        if renglon[0][0] == "?":
            while renglon[0][-1] != "?":
                creacion += renglon[0] + " "
                renglon.pop(0)
            creacion += renglon[0]
            preguntas.append(creacion)
            creacion = ""
            renglon.pop(0)
        else:
            renglon.pop(0)
    return preguntas

texto = open("Diálogos del agente Smith.txt", "r")
preguntas_unificadas = []
for renglon in texto:
    if "?" in renglon:
        if "Smith" in renglon:
            renglon = renglon.split()
            parcial = pregunta(renglon)
            for preg in parcial:
                if preg not in preguntas_unificadas:
                    preguntas_unificadas.append(preg)
for i in preguntas_unificadas:
    print(i)
texto.close
