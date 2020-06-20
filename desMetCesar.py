#!/usr/bin/python3

def main():
    llave = input("Inserte Llave:")
    archivo = open('cifrado.txt', 'r')
    ctexto = archivo.read()
    texto_plano = ""
    for index,val in enumerate(ctexto):
        c = ord(val) ^ ord(llave[0])
        texto_plano += str(chr(c))
    print("Text Plano:")
    print(texto_plano)
main()