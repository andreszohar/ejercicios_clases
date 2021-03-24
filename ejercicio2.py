# se desea reclutar personal para los cargos de analista, desarrollador, arquitecto de software y el salario para cada uno tiene un estimado de la siguiente manera
# analista 870000, arquitecto 790000, desarrollador :2300000, se requiere saber el numero de personas que se presentan para cada uno de los cargos y conocer cuanto seria el costo de inversion segun la cantidad de personas que se presentan.


analista=870000
arquitecto=790000
desarrollador=2300000
reclutadoAnalista=0
reclutadoArquitecto=0
reclutadoDesarrollador=0

centinela=input("Deseas ingresar a la compañia (si/no): ")

while(centinela=="si"):

    
    cargo=input("Analistas==>1  Arquitecto==>2  Desarrollador==>3: ")

    if(cargo=="1"):
        reclutadoAnalista=reclutadoAnalista+1
    
    if(cargo=="2"):
        reclutadoArquitecto=reclutadoArquitecto+1

    if(cargo=="2"):
        reclutadoDesarrollador=reclutadoDesarrollador+1

    centinela=input("Deseas ingresar a la compañia (si/no): ")


print("la cantidad de Analistas es: " ,reclutadoAnalista)
print("precio total por los  Analistas: " ,analista*reclutadoAnalista,"$")

print("la cantidad de Arquitectos es: " ,reclutadoArquitecto)
print("precio total por los  Arquitectos: " ,arquitecto*reclutadoArquitecto,"$")

print("la cantidad de Desarrolladores es: " ,reclutadoDesarrollador)
print("precio total por los  Analistas: " ,desarrollador*reclutadoDesarrollador,"$")






    

    
