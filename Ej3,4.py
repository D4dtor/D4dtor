print("1")
cantidad=100

for i in range(2,cantidad):
    esprimo=1
    
    for x in range(2,i-1):
        if(i%x==0):
            esprimo=0
            break
    if(esprimo==1):
        print(i)
            
        

    
            
            