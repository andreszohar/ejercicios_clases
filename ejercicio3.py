#Se necesita conocer e numero de personas que asisten a comfama de las ballenitas y conocer el porcentaje de adultos, niños que ingresan al parque, la clasificacion de niños esta desde  el mes de nacido hasta 15 niño- joven de 16 a 18, y adulto de 18 en adelante. 

nino=0
adultos=0
jovenes=0
centinela=input("asistencia si o no: ")


while(centinela=="si"):

    edad=int(input("ingrese edad: "))
    if(edad<=15 and edad>1):
        nino=nino+1
    if(edad>=16 and edad<18):
        adultos=adultos+1
    if(edad>=18):
        jovenes=jovenes+1

    
    centinela=input("asistencia si o no: ")

if(nino>=1):
    porcentajeNinos=nino*33.3
if(nino==0):
    porcentajeNinos=0
if(adultos>=1):
    porcentajeAdultos=adultos*33.3
if(adultos==0):
    porcentajeAdultos=0
if(jovenes>=1):
    porcentajeJovenes=jovenes*33.3
if(nino==0):
    porcentajeJovenes=0

print("El porcentaje de niños frente a los tres grupos es: ",porcentajeNinos,"%")
print("El porcentaje de jovenes frente a los tres grupos es: ",porcentajeJovenes,"%")
print("El porcentaje de Adultos frente a los tres grupos es: ",porcentajeAdultos,"%")