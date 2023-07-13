carga_telaraña = float(input())
cantidad_elefantes = int(input())
contador_elefantes = 0
peso_elefante_2 = 0
for i in range (1, cantidad_elefantes+1) :
    peso_elefante = float(input())
    peso_elefante_2 += peso_elefante
    if peso_elefante_2 > carga_telaraña :
        continue
    contador_elefantes += 1
print(contador_elefantes)
