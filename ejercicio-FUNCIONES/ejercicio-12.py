# escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas 
# con la sigientes forma

# [("manuel juares", 1222333 "liverpool"),("silva paredes"
# ,0233333,"buenos aires" "rosa ortiz 000000044"")] ets

# ademas en otra lista de tuplas se almacena los datos de cada ciduad y el pais al que pertenece,ejemplo
# [("manuel juares", 1222333 "liverpool"),("silva paredes"
# ,0233333,"buenos aires" "rosa ortiz 000000044"")] ets

# hacer un menu iterativo que permita al usuario realizar las siguientes operaciones
# agregar pasajeros ala lista de viajeros
# agregar ciduades ala lista de ciudades
# dado la cedula de un pasajero ver a que ciudad viaja
# dada la ciudad mostrar la cantidad de pasajeros que viajan a esa ciudad
# dado la cedula de un pasajero ver a que pais viaja
# dado un pais mostra cuantos pasajeros viajan a ese pais
# salir del programa
def agregarpasajeros (pasajeros):
        nombre=input("nombre -x para cortar:")
        while nombre != "x":
            cedula=int(input("cedula:"))
            destino=input("ciudad destino:")
            pasajeros.append((nombre , cedula, destino))
            nombre=input("nombre -x para cortar:")
            return pasajeros   


def agregarciudades(ciudades):
    '''agrega ciudades ala lista y la retorna'''
    ciudad=input("ciudad -x cortar:")
    while ciudad!="x":
        pais=input("pais:")
        ciudades.append((ciudad,pais))
        ciudad=input("ciudad -x para cortar:")
        return ciudades

       
def buscarciudad(pasajeros,cedula):
    '''dado la cedula de un pasajero lo busca en la lista y retorma la ciudad ala que viaja
    si no se encuentra la cedula retorna string vacio'''
    for viaje in pasajeros: 
        if viaje[1]==cedula:
            return viaje[2]
    return ""

def cantidadpasajerosciudad(pasajeros,ciudad):
    '''dada una lista de pasajeros y una ciudad retorna la cantidad de pasajeros que viajan 
    a esa ciudad'''
    cantidad=0
    for viaje in pasajeros:
        if viaje[2]==ciudad:
            cantidad+=1
    return cantidad    


def buscarpaisdestino(pasajeros,ciudades,cedula):
    '''dada una lista de pasajeros una de ciudades y un cedula retorma el pais al que viaja el 
    pasajero con esa cedula'''
    ciudadbuscadar=buscarciudad(pasajeros,cedula)
    for ciudad in ciudades:
        if ciudad[0]==ciudadbuscadar:
            return ciudad[1]
    return "" 

def cantidadpasajerospais(pasajeros,ciudades,pais):
    '''dada una lista de pasajeros una ciudades y un pais retorma la cantidad de pasajeros que 
    viajan a ese pais'''
    cantidad=0
    for viaje in pasajeros:
        if pais==buscarpaisdestino(pasajeros,ciudades,viaje[1]):
            cantidad+=1
    return cantidad  

pasajeros=[]
ciudades=[]
while True:
    print("1.agregar pasajeros")
    print("2.agregar ciudades")
    print("3.buscar ciudad destino mediante la cedula")
    print("4.cantidad de pasajeros que viajan a una ciudad")
    print("5.buscar pais destino mediante cedula")
    print("6.cantidas de pasajeros que viajan a un pais")
    print("7.salir del programa")
    opcion=int(input("accion a ejecutar:"))
    if opcion ==1:
        print("agregar pasajeros")
        pasajeros=agregarpasajeros(pasajeros)

    elif opcion ==2:
        print("agregar ciudades")
        ciudades=agregarciudades(ciudades)

    elif opcion ==3:
        cedula=int(input("cedula: "))
        print("e pasajero viaja a ",buscarciudad(pasajeros,cedula))

    elif opcion ==4:
        ciudad=input("ciudad: ")
        print("viaja ",cantidadpasajerosciudad(pasajeros,ciudad),"pasajeros")
                  
    elif opcion ==5:  
        cedula=int(input("cedula: "))
        print("viajan",buscarpaisdestino(pasajeros,ciudades,cedula))

    elif opcion ==6: 
        pais=input("pais: ")
        print("viajan", cantidadpasajerospais(pasajeros,ciudades,pais),"pasajeros")

    elif opcion ==7:
        break
    else:
        print("opcion invalidad")



