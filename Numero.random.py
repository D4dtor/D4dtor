import random
x= random.randint(0,100)
vidas=3

while(vidas>=1):
    a=int(input("Dime un numero: "))
    if(a==x):
        print("Has acertado el numero, has ganado")
        break
    else:
        vidas=vidas-1
        print("Has fallado te quedan ",vidas," intentos")
        if(vidas==0):
            print ("Has perdido")
    