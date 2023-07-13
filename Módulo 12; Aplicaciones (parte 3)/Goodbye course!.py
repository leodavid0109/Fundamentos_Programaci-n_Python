def idioma(codigo):
    idiomas = {0:"Español", 1:"Inglés", 2:"Francés", 3:"Portugués", 4:"Alemán"}
    idioma = idiomas[codigo]
    return idioma

def despedida(idioma):
    mensajes = {"Español":"Hasta luego curso! Turing, puedes estar orgulloso de mi", "Inglés":"Goodbye course! Turing, you can be proud of me", "Francés":"Au revoir cours! Turing, tu peux etre fier de moi", "Portugués":"Adeus, curso! Turing, pode se orgulhar de mim", "Alemán":"Auf Wiedersehen! Turing, du kannst stolz auf mich sein"}
    mensaje = mensajes[idioma]
    return mensaje

entero = int(input())
while entero >= 5:
    ingreso = entero % 5
    mensaje = despedida(idioma(ingreso))
    print(mensaje)
    entero = entero // 5
