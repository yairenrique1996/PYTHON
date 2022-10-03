#Escribir un programa que pida al usuario dos números y muestre 
# por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

num1 = float(input("Introduce el dividendo: "))
num2 = float(input("Introduce el divisior: "))
if num2 == 0:
    print("¡Error! No se puede dividir por 0.")
else:
    print(num1/num2)
