# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
#  pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la 
# divisa no está en el diccionario.


# monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# moneda = input("Introduce una divisa: ")
# print(monedas.get(moneda.title(), "La divisa no está."))

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("La divisa no está.")