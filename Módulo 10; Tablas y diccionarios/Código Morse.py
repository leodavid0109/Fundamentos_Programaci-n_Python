def codificador(frase):
    braile = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--..", ".":".-.-.-", ",":"-.-.--", " ":"/"}
    frase = frase.lower()
    for i in range(len(frase)):
        print(braile[frase[i]], end = " ")

cantidad = int(input())
for i in range(cantidad):
    frase = input()
    codificador(frase)
    print("\n")
