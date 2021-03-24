#pedir destino, numero de personas, calcular total
#se desea numero de personas por destino y porcentaje por destino

###########islas
capurgana=2525000
nuqui=1536000
islamargaritaDolares=200
islamargaritaPesos=723900
islagalapagosDolares=400
islagalapagosPesos=1447800
mukura=1440000
islasanandres=1875000



print("...................Agencia de Viajes Aviatour.............")
centinela=input("Encender aplicación ( SI=1   NO=2 ): ")


contadorPrincipal=0
contCapurgana=0
contNuqui=0
contMukura=0
contSanAndres=0
contMargarita=0
contGalapagos=0

totalpersonas_capurgana=0
totalpersonas_nuqui=0
totalpersonas_mukura=0
totalpersonas_sanAndres=0
totalpersonas_Margaritas=0
totalpersonas_Galapagos=0
total_turistas=0




while(centinela=="1"):


    print('"1" = capurgana 1.500.000 más impuestos ')
    print('"2" = nuqui  1200000 más impuestos')
    print('"3" = isla margarita  ')
    print('"4" = isla galapago  ')
    print('"5" = isla mukura  1200000 más impuestos')
    print('"6" = isla san andres 1500000 más impuestos ')
    viajar=input("Elige tu destino TRAVEL:  ")

    

    if(viajar=="1"):
        contCapurgana=contCapurgana+1
        conteoPersonasCapurgana=int(input("Ingrese cantidad de personas: "))
        tpersonasCapurgana=conteoPersonasCapurgana*capurgana
        print("El total a pagar por el Viaje es de: "+str(tpersonasCapurgana)+"$")

        totalpersonas_capurgana=totalpersonas_capurgana+conteoPersonasCapurgana

    elif(viajar=="2"):
        contNuqui=contNuqui+1
        conteoPersonasNuqui=int(input("Ingrese cantidad de personas: "))
        tpersonasNuqui=conteoPersonasNuqui*nuqui
        print("El total a pagar por el Viaje es de: "+str(tpersonasNuqui)+"$")

        totalpersonas_nuqui=totalpersonas_nuqui+conteoPersonasNuqui

    elif(viajar=="5"):
        contMukura=contMukura+1
        conteoPersonasMukura=int(input("Ingrese cantidad de personas: "))
        tpersonasMukura=conteoPersonasMukura*mukura
        print("El total a pagar por el Viaje es de: "+str(tpersonasMukura)+"$")

        totalpersonas_mukura=totalpersonas_mukura+conteoPersonasMukura
    
    elif(viajar=="6"):
        contSanAndres=contSanAndres+1
        conteoPersonasSanAndres=int(input("Ingrese cantidad de personas: "))
        tpersonasSanAndres=conteoPersonasSanAndres*islasanandres
        print("El total a pagar por el Viaje es de: "+str(tpersonasSanAndres)+"$")

        totalpersonas_sanAndres=totalpersonas_sanAndres+conteoPersonasSanAndres

    elif(viajar=="4"):
        contMargarita=contMargarita+1
        conteoPersonasMargaritas=int(input("Ingrese cantidad de personas: "))

        respuestamargaritas=input("Desea saber el valor en pesos==1 o dolares==2")
        if(respuestamargaritas=="1"):
            tpersonasMargaritas=conteoPersonasMargaritas*islamargaritaPesos
            print("El total a pagar por el Viaje es de: "+str(tpersonasMargaritas)+"$")
        else:
            tpersonasMargaritas=conteoPersonasMargaritas*islamargaritaDolares
            print("El total a pagar por el Viaje es de: "+str(tpersonasMargaritas)+"Dolare$")

        totalpersonas_Margaritas=totalpersonas_Margaritas+conteoPersonasMargaritas
    
    elif(viajar=="5"):
        contGalapagos=contGalapagos+1
        conteoPersonasGalapagos=int(input("Ingrese cantidad de personas: "))

        respuestaGalapagos=input("Desea saber el valor en pesos==1 o dolares==2")
        if(respuestaGalapagos=="1"):
            tpersonasGalapagos=conteoPersonasGalapagos*islagalapagosPesos
            print("El total a pagar por el Viaje es de: "+str(tpersonasGalapagos)+"$")
        else:
            tpersonasGalapagos=conteoPersonasGalapagos*islagalapagosDolares
            print("El total a pagar por el Viaje es de: "+str(tpersonasGalapagos)+"Dolare$")

        totalpersonas_Galapagos=totalpersonas_Galapagos+conteoPersonasGalapagos



    






    contadorPrincipal=contadorPrincipal+1
    centinela=input("Mantener aplicación Encendida ( SI=1   NO=2 ): ")

total_turistas=totalpersonas_capurgana+totalpersonas_nuqui+totalpersonas_mukura+totalpersonas_sanAndres+totalpersonas_Margaritas+totalpersonas_Galapagos

print("El total de turistas es de: "+ str(total_turistas))

print("El total de turistas en Capurgana es de "+str(totalpersonas_capurgana))
print("El total de turistas en Nuqui es de "+str(totalpersonas_nuqui))
print("El total de turistas en Mukura es de "+str(totalpersonas_mukura))
print("El total de turistas en San Andres es de "+str(totalpersonas_sanAndres))
print("El total de turistas en las islas Margaritas es de "+str(totalpersonas_Margaritas))
print("El total de turistas en las islas Galapagos es de "+str(totalpersonas_Galapagos))



numero=float(16.7)

porcentajeCapurgana=round(totalpersonas_capurgana*numero)/100
porcentajeNuqui=round(totalpersonas_nuqui*numero)/100
porcentajeMukura=round(totalpersonas_mukura*numero)/100
porcentajeSanAndres=round(totalpersonas_sanAndres*numero)/100
porcentajeMargaritas=round(totalpersonas_Margaritas*numero)/100
porcentajeGalapagos=round(totalpersonas_Galapagos*numero)/100



print("El porcentaje de turistas en Capurgana es de "+str(porcentajeCapurgana)+"%")
print("El porcentaje de turistas en Nuqui es de "+str(porcentajeNuqui)+"%")
print("El porcentaje de turistas en Mukura es de "+str(porcentajeMukura)+"%")
print("El porcentaje de turistas en San Andres es de "+str(porcentajeSanAndres)+"%")
print("El porcentaje de turistas en Islas Margaritas es de "+str(porcentajeMargaritas)+"%")
print("El porcentaje de turistas en Galapagos es de "+str(porcentajeGalapagos)+"%")

















