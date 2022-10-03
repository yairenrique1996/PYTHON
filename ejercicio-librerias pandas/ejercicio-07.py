# El fichero titanic.csv contiene información sobre los pasajeros del Titanic. 
# Escribir un programa con los siguientes requisitos:

# Generar un DataFrame con los datos del fichero.
# Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene,
#  los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras 
#  filas y las 10 últimas filas
# Mostrar por pantalla los datos del pasajero con identificador 148.
# Mostrar por pantalla las filas pares del DataFrame.
# Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas 
# alfabéticamente.
# Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
# Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
# Eliminar del DataFrame los pasajeros con edad desconocida.
# Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
# Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
# Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.


# import pandas as pd

# # Generar un DataFrame con los datos del fichero.
# titanic = pd.read_csv('https://raw.githubusercontent.com/asalber/asalber.github.io/master/python/ejercicios/soluciones/pandas/titanic.csv', index_col=0)

# print(titanic)

