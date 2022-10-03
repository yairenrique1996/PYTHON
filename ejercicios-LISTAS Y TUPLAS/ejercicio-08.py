# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

palabra = input("Introduce una palabra: ")
palabra1 = palabra
lista = list(palabra)
palabra1 = list(palabra1)
palabra1.reverse()
if lista == palabra1:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")