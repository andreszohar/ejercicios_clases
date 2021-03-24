#Aplicativo de Sobre peso de acuerdo a la edad, peso y altura

cantidadPersonas=int(input("Ingrese la cantidad de personas ó presiona 0 + Enter para terminar: "))
n=1



while(n<=cantidadPersonas):
    edad=int(input("Ingrese edad de la persona "+str(n)+": " ))
    Peso=float(input("Ingrese el peso con punto de la persona "+str(n)+": " ))
    estatura=float(input("Ingrese estatura de la persona "+str(n)+": " ))
    imc=round(Peso/(estatura)**2)
    
    if(imc<=25):
        print("Usted tiene un peso adecuado")
    
    else:
        print("Usted es obeso")



    n=n+1
    

