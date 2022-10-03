# crear un programa para gestionar datos de socios de un clud permitiendo

# cargar informacion de los socios en un diccionario para acceder por numero de socios los socios 
# los datos a almacenar son numero nombre y apelido fecha ingreso (ddmmaa) cuota al dia (s/n) el programa
# debe iniciar con los datos de los socios fundadores ya cargados 

# socio n#1 amanda muñes ingraso 17/03/2009 cuota al dia
# socio n#2 barbara molina ingreso 17/03/2009 couta al dia 
# socio n#3 lautaro campos ingreso 17/03/2009 cuota al dia 

# informar cantidad de socios del clud 

# solicitar al usuario el numero de un socio y registrar que ha pagado todas la cuotas adeudadas

# modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018 para indicar que en Realidad 
# ingresaron el 14/03/2018
# solicitar el nombre y apelido de un socio y darlo de baja (eliminarlo del listado)

# imprimir el listado de socios completo
def cargarsocios(socios):
    numero=int(input("numero de socio: "))
    while numero !=0:
        nombre=input("nombre y apellido: ")
        fecha=input("fecha de ingreso: ")
        cuota=input("¿cuota al dia ? s/n ")
        pago=cuota.lower()=="s"
        socios[numero]=[nombre,fecha,pago]
        numero=int(input("numero de socio: "))
    return socios      


def modificarfecha(socios,fecha_anterior,fecha_nueva):
    for datos in socios.values():
        if datos[1]==fecha_anterior:
            datos[1]=fecha_nueva
    return socios


def  numerosocio(socios,nombre):
    for numero,datos in socios.items():
        if datos[0].lower()==nombre.lower():
            return numero
    return 0 

def formatofecha(fecha):
    return fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:]

def imprimirlistado(socios):
    for numeros,datos in socios.items():
        print("numero : " , numero)
        print("-numero : " , datos[0])
        print("-fecha de ingreso : " , formatofecha(datos[1]))
        if datos[2]:
            print("cuota al dia")
        else:
         print("en deuda")
        print("----------------")
    return None   


socios_activos={1:["amanda nuñez","17032009", True],2:["barbara molina","17032009",True],3:["LAUTARO campos","17032009",True]}
print("***cargar socios")
socios_activos=cargarsocios(socios_activos)

print("el clud tiene",len(socios_activos),"socios")
print("**registar pago de cuotas")
numero=int(input("numero de socios: "))
socios_activos[numero][2]=True

print("***modificando fecha de ingreso...")
socios_activos=modificarfecha(socios_activos, "13032018","14032018")

print("****eliminar socio:")
nombre=input("nombre y apellido:")
numero=numerosocio(socios_activos,nombre)
del socios_activos[numero]

imprimirlistado(socios_activos)




