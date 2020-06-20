#!/usr/bin/python3

def main():

    texto = input("inserte texto plano:")
    llave = input("inserte llave:")
    texto_cif = obtener_cifrado(llave,texto)
    archivo = open('cifrado.txt', 'w')
    archivo.write(texto_cif)

def obtener_cifrado(llave,texto_plano):
    cif = ""
    for index,val in enumerate(texto_plano):
        c = ord(val) ^ ord(llave[0])
        cif += str(chr(c))
    return cif
main()
