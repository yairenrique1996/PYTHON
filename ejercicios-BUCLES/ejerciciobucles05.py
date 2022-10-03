#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el 
# número de años, y muestre por pantalla 
# el capital obtenido en la inversión cada año que dura la inversión.
cantiinver = float(input("¿Cantidad a invertir? "))
interses = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
for i in range(años):
    cantiinver *= 1 + interses / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(cantiinver, 2)))