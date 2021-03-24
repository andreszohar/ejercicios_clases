#mostrar la serie fibonaci

n=0
num=1
ultimo=0
antesUltimo=0


while(n<=15):
    print(n,"=",num)
    antesUltimo=ultimo
    ultimo=num
    num=antesUltimo+ultimo
    

    n=n+1