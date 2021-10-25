"""3.2 Introduciendo un número en el teclado de ordenador, hallar cuantos números enteros múltiplos de tres, hay comprendidos entre la unidad y dichonúmero."""
a=int(input("Dime un numero: "))
x=0

res=x*3

while(res<a-2):
    
    x=x+1
    res=x*3
    
    
    
print("El numero de multiplos de 3 que habrá será o serán: ",x)
