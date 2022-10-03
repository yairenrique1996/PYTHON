def sumatoria(lista):
    suma=0
    for n in lista:
        suma+=n
    return suma

def numerosmenores(lista,limite):
    nueva=[]
    for n in lista:
        if n<limite:
            nueva.append(n)
    return nueva

def frecuencia(lista):
    nueva=[]
    for n in lista:
        if (n,lista.count(n)) not in nueva:
            nueva.append((n,lista.count(n)))   
    return nueva                         




numeros=[]
nro=int(input("numero: "))
while nro !=0:
    numeros.append(nro)
    nro=int(input("numeros: "))


eliminar=int(input("numero a eliminar:"))
if eliminar in numeros:
    numeros.remove(eliminar)

else:
    print("ese numero no esta entre los ingresados")        



print("sumatoria de los numeros ",sumatoria(numeros))    

limite=int(input("filtrar numeros a : "))
for n in numerosmenores(numeros,limite):
    print(n)


print("frecuencia: ")
for tupla in frecuencia(numeros):
    print(tupla[0],"aparece",tupla[1],"veces")    