'''2.1. Escriba, usando comparaciones, un algoritmo que muestre el estado delagua (hielo, liquido, vapor) en función de su temperatura.'''

t=int(input("Dime la temperatura: "))

if(t<0):
      print("El agua está en estado solido",t)

else:
      if(t<100):
          print("El agua está en estado liquido",t)
      else:
          print("El agua está en estado gaseoso",t)
