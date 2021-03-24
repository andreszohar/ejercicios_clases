#El estadio atanasio girardot realizará el clasico de la montaña, se requiere
#saber el numero de boletas que se venden conociendo que la capacidad del estadio 
#es de 45000, pero no se vende necesariamente el total de boletas, ademas conocer
#el numero de personas que ingresaron a tribuna norte,sur, oriente, occidente
#el numero de mujeres y hombres que ingresaron.

totalBoletas=0
norte=0
sur=0
oriente=0
h=0
m=0

boleta=input("Quieres comprar entrada= si==1   no==2: ")

while(boleta=="1"):
    tribuna=input("Tribuna Norte=1 sur=2 oriente=3: ")

    if(tribuna=="1"):
        norte=norte+1
    if(tribuna=="2"):
        sur=sur+1
    if(tribuna=="3"):
        oriente=oriente+1
    
    sexo=input("Eres hombre=1 mujer=2: ")

    if(sexo=="1"):
        h=h+1
    if(sexo=="2"):
        m=m+1

    totalBoletas=totalBoletas+1
    boleta=input("Quieres comprar entrada= si==1   no==2: ")

print("la cantidad de boletas vendidas es de: ",totalBoletas)
print("cantidad de personas por tribuna")
print("Norte= ",norte," sur: ",sur," oriente: ",oriente)
print("cantidad de Mujeres y Hombres")
print("Hombres= ",h," Mujeres: ",m)
