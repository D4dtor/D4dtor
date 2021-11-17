def genera(num_f,num_c,valor):
    return[[valor for c in range(0,num_c)] for f in range(0,num_f)]

juego=genera(3,3,0)


def mostrar(juego):
    print("-------------")
    print("|",juego[0][0],"|",juego[0][1],"|",juego[0][2],"|")
    print("-------------")
    print("|",juego[1][0],"|",juego[1][1],"|",juego[1][2],"|")
    print("-------------")
    print("|",juego[2][0],"|",juego[2][1],"|",juego[2][2],"|")
    print("-------------")



def empezar(juego):
    x=0
    for i in juego:
        for a in i:
            if(a==0):
                x=x+1
    print(x)

    while(x>=1):
        print(mostrar(juego))
        if(x%2==0):
            print("En que posicion lo quieres colocar tu 1")
            f=int(input("Escribe el numero de tu fila entre 1 y 3: "))
            c=int(input("Escribe el numero de tu columna entre 1 y 3: "))
            f=f-1
            c=c-1
            if(juego[f][c]==0):
                juego[f][c]=1
                if((juego[0][0]==1) and (juego[1][0]==1) and (juego[2][0]==1)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 1")
                    x=0
                if((juego[0][1]==1) and (juego[1][1]==1) and (juego[2][1]==1)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 1")
                    x=0
                if((juego[0][2]==1) and (juego[1][2]==1) and (juego[2][2]==1)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 1")
                    x=0
                if((juego[0][0]==1) and (juego[0][1]==1) and (juego[0][2]==1)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 1")
                    x=0
                if((juego[1][0]==1) and (juego[1][1]==1) and (juego[1][2]==1)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 1")
                    x=0
                if((juego[2][0]==1) and (juego[2][1]==1) and (juego[2][2]==1)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 1")
                    x=0
                if((juego[0][0]==1) and (juego[1][1]==1) and (juego[2][2]==1)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 1")
                    x=0
                if((juego[2][0]==1) and (juego[1][1]==1) and (juego[0][2]==1)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 1")
                    x=0
                if((juego[0][0]==2) and (juego[1][0]==2) and (juego[2][0]==2)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 2")
                    x=0
                if((juego[0][1]==2) and (juego[1][1]==2) and (juego[2][1]==2)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 2")
                    x=0
                if((juego[0][2]==2) and (juego[1][2]==2) and (juego[2][2]==2)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 2")
                    x=0
                if((juego[0][0]==2) and (juego[0][1]==2) and (juego[0][2]==2)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 2")
                    x=0
                if((juego[1][0]==2) and (juego[1][1]==2) and (juego[1][2]==2)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 2")
                    x=0
                if((juego[2][0]==2) and (juego[2][1]==2) and (juego[2][2]==2)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 2")
                    x=0
                if((juego[0][0]==2) and (juego[1][1]==2) and (juego[2][2]==2)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 2")
                    x=0
                if((juego[2][0]==2) and (juego[1][1]==2) and (juego[0][2]==2)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 2")
                    x=0
                else:
                    x=x-1
                
            else:
                print("Elige una posicion vacia")
        else:
            print("En que posicion lo quieres colocar tu 2")
            f=int(input("Escribe el numero de tu fila entre 1 y 3: "))
            c=int(input("Escribe el numero de tu columna entre 1 y 3: "))
            f=f-1
            c=c-1
            if(juego[f][c]==0):
                juego[f][c]=2
                if((juego[0][0]==1) and (juego[1][0]==1) and (juego[2][0]==1)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 1")
                    x=0
                if((juego[0][1]==1) and (juego[1][1]==1) and (juego[2][1]==1)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 1")
                    x=0
                if((juego[0][2]==1) and (juego[1][2]==1) and (juego[2][2]==1)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 1")
                    x=0
                if((juego[0][0]==1) and (juego[0][1]==1) and (juego[0][2]==1)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 1")
                    x=0
                if((juego[1][0]==1) and (juego[1][1]==1) and (juego[1][2]==1)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 1")
                    x=0
                if((juego[2][0]==1) and (juego[2][1]==1) and (juego[2][2]==1)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 1")
                    x=0
                if((juego[0][0]==1) and (juego[1][1]==1) and (juego[2][2]==1)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 1")
                    x=0
                if((juego[2][0]==1) and (juego[1][1]==1) and (juego[0][2]==1)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 1")
                    x=0
                if((juego[0][0]==2) and (juego[1][0]==2) and (juego[2][0]==2)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 2")
                    x=0
                if((juego[0][1]==2) and (juego[1][1]==2) and (juego[2][1]==2)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 2")
                    x=0
                if((juego[0][2]==2) and (juego[1][2]==2) and (juego[2][2]==2)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 2")
                    x=0
                if((juego[0][0]==2) and (juego[0][1]==2) and (juego[0][2]==2)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 2")
                    x=0
                if((juego[1][0]==2) and (juego[1][1]==2) and (juego[1][2]==2)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 2")
                    x=0
                if((juego[2][0]==2) and (juego[2][1]==2) and (juego[2][2]==2)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 2")
                    x=0
                if((juego[0][0]==2) and (juego[1][1]==2) and (juego[2][2]==2)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 2")
                    x=0
                if((juego[2][0]==2) and (juego[1][1]==2) and (juego[0][2]==2)):
                    print(mostrar(juego))
                    print("Ha ganado el jugador 2")
                    x=0
                else:
                    x=x-1
                
            else:
                print("Elige una posicion vacia")
                
    print(mostrar(juego))
    print("fin del juego")
        
