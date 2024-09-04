num = int(input("ingresa un numero: "))
facotiral = 1
while num >= 2:
    facotiral *= num * (num - 1)
    num = num - 2 
print(facotiral)    
    