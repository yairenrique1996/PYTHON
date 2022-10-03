def dolares():
    print("cual es el precio del dolar el dia de hoy")
    global precioD
    precioD=input()
    precioD = float(precioD)
    global dinerito
    dinerito = pesos/precioD
    print("tienes",dinerito,"dolares")


def dolares_can():
    print("cual es el precio del dolar canadiens el dia de hoy")
    global precioD
    precioD =input()
    precioD = float(precioD)
    global dinerito
    dinerito = pesos/precioD
    print("tienes",dinerito,"dolares canadiense")    

    menu()

    global cambio
    cambio = input()
    cambio = int (cambio)

    # evaluando tipo de cambio 
    if (cambio ==1):
        dolares()
    elif (cambio==2):
        dolares_can()
        print("tienes",dinerito,"dolares canadiense")

# definiendi la funcion euros
def euros():
    print("cual es el precio del euro el dia de hoy")
    global precioE 
    precioE =input()
    precioE=float(precioE)
    global dinerito
    dinerito = pesos/precioE
    print("tienes ",dinerito,"euros") 
    menu()    
    dolares_can()
  elif (cambio ==3):      
    euros()          


def menu():
    print("1.Dolar")
    print("2.Dolar canadiense")
    print("3.euro")
    print("4.libra esterlina")
    print("5.centenario")
    print("cuantos pesos tiene")
    global pesos 
    pesos=input()
    pesos=float(pesos)
    print("que tipo de cambio deseas realizar")
    global cambio 
    cambio =input()
    cambio =input(cambio)

    # evalucando el tipo de cambio
    if(cambio==1):
        print("cual es el precio del dolar el dia de hoy")
        global precioD 
        precioD =input()
        precioD =float(precioD)
        global dinerito 
    dinerito =pesos/precioD
    print("tienes",dinerito,"dolares")
