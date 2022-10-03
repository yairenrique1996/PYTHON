# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de 
# veces que contiene
#  cada vocal.

palabra = input("Introduce una palabra: ")
vocal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for vocal in vocal: 
    veces = 0
    for letter in palabra: 
        if letter == vocal:
            veces += 1
    print("La vocal " + vocal + " aparece " + str(veces) + " veces")