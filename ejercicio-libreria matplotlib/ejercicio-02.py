# Escribir una función que reciba una diccionario con las notas de las asignaturas de 
# un curso y una cadena con el nombre de un color y devuelva un diagrama de barras de las
#  notas en el color dado.

# import matplotlib.pyplot as plt 

# def diagrama_barras_notas(notas, color):
#     '''Función que construye un diagrama de barras con las notas de las asignaturas de un curso.
    
#     Parámetros:
#         - notas: Es un diccionario formado por pares con clave el nombre de la asignaturay valor la nota.
#         - color: Es una cadena con el color de las barras.
    
#     Salida:
#         - Un diagrama de barras con las notas del diccionario dado en el color dado.
#     '''
#     # Definimos la figura y los ejes del gráfico con Matplotlib
#     fig, ax = plt.subplots()
#     # Dibujamos las barras con las notas a partir del diccionario
#     ax.bar(notas.keys(), notas.values(), color = color)
#     # Devolvemos un objeto con los ejes y las barras que contienen
#     return ax

# notas = {'Programación':9, 'Mates':6.5, 'Economía':4, 'Historia': 8}
# diagrama_barras_notas(notas, 'orange')
# plt.show()