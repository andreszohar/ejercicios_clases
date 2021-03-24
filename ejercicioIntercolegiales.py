#por colegios se de inscribir una pareja, y cada estudiante el grado y la edad.
#Obtener cantiidad de colegios, cantidad de niños y niñas

colegios=0
pareja=0
estudiante=0
contador1=1
nino=0
nina=0



colegios=int(input("Ingrese la cantidad de colegios: "))

while(contador1<=colegios):
    nombreColegio=input("Ingrese el nombre del Colegio: ")


    contador2=1
    while(contador2<=2):
        grado=input("En que grado estas alumno "+str(contador2)+": ")
        edad=input("Cual es tu edad: ")

        pregunta=input("Niño===>1   Niña===>2  :> ")
        if(pregunta=="1"):
            nino=nino+1
        else:
            nina=nina+1
        

        contador2=contador2+1
    
    contador1=contador1+1

print("La cantidad de colegios es: "+str(colegios))
print("La cantidad de niños es: "+str(nino))
print("La cantidad de niñas es: "+str(nina))






