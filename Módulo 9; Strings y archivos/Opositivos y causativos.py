def opositivos(texto) :
    texto = texto.lower()
    sin_embargo = texto.count("sin embargo")
    no_obstante = texto.count("no obstante")
    ahora_bien = texto.count("ahora bien")
    aun_asi = texto.count("aun asi")
    opositivo = sin_embargo + no_obstante + ahora_bien + aun_asi
    return opositivo

def causativos(texto) :
    texto = texto.lower()
    por_tanto = texto.count("por tanto")
    dado_que = texto.count("dado que")
    por_consiguiente = texto.count("por consiguiente")
    asi_pues = texto.count("asi pues")
    por_ende = texto.count("por ende")
    causativo = por_tanto + dado_que + por_consiguiente + asi_pues + por_ende
    return causativo

texto = open("Opositivos y causativos.txt", "r")
for renglon in texto :
    print("Opositivos", opositivos(renglon), "Causativos", causativos(renglon))
texto.close()
