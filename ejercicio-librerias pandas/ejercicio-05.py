# Escribir una función que reciba un DataFrame con el formato del ejercicio anterior, una 
# lista de meses, y devuelva el balance (ventas - gastos) total en 
# los meses indicados.

# import pandas as pd

# datos = {'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'], 'Ventas':[30500, 35600, 28300, 33900], 'Gastos':[22000, 23400, 18100, 20700]}

# contabilidad = pd.DataFrame(datos)

# def balance(contabilidad, meses):
#     contabilidad['Balance'] = contabilidad.Ventas - contabilidad.Gastos
#     return contabilidad[contabilidad.Mes.isin(meses)].Balance.sum()

# print(balance(contabilidad, ['Enero','Marzo']))