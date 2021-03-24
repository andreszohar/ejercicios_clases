#Ejercicio clase cantidad de mujeres y hombres

contador1=0
contador2=0
centinela=input("ingrese si o no: ")


while(centinela=="si"):

    genero=input("ingrese m o f:")
    if(genero=="m"):
        contador1=contador1+1
    if(genero=="f"):
        contador2=contador2+1
    centinela=input("ingrese si o no: ")

print("La cantidad de mujeres y hombres es iguala a: ",contador1+contador2)
print("La cantidad de mujeres es: ",contador2)
print("La cantidad de HOMBRES es: ",contador1)


