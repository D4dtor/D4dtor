"""2.2. Escriba un algoritmo que determine la categoría deportiva de
un usuario en función de su edad.- 6 a7 años: “benjamin”- 8 a 9 años:
“ alevín”- 10 a 11 años: “infantil”- 12 años y más: “cadete”"""
n=int(input("Dime la edad y te digo su categoria deportiva: "))
print(n)

if(n<6):
    print("Su hijo es muy pequeño para estar en una categoria deportiva")
else:
    if(n<=7):
        print("Su hijo es Benjamin")
    else:
        if(n<=9):
            print("Su hijo es alevin")
        else:
            if(n<=11):
                print("Su hijo es infantil")
            else:
                if(n>=12):
                    print("Su hijo es cadete")
                else:
                    print("Otro")
    

