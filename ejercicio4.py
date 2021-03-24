#Se requiere saber el numero de personas qe ingresan a un lavadero de vehiculos,  y establecer la cantidad de de personas por cada uno de los servicios, si el servicio es sencillo o full, si el sencillo tiene un costo de 12000 y el full de 17000, ¿cual es la cantidad de dinero que se recolecto por cada uno de los servicios?

sencillo=12000
contSencillo=0
full=17000
contFull=0
centinela=input("ingreso al lavdero de carros si o no: ")


while(centinela=="si"):
    tipo=input("Sencillo=1   Full=2 => ")

    if(tipo=="1"):
        contSencillo=contSencillo+1
    if(tipo=="2"):
        contFull=contFull+1
    centinela=input("ingreso al lavdero de carros si o no: ")
    
    


print("la cantidad de servicios sencillos es de ",contSencillo," y el total ganado es de ",contSencillo*sencillo)

print("la cantidad de servicios full es de ",contFull," y el total ganado es de ",contFull*full)







    

    