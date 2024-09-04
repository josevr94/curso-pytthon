lista = [18, 3, 34, 12, 30, 19, 12, 11, 0, 34]

for i in lista:
    if i == 0:
        print(f"El numero {i} es cero") 
    elif i % 2 == 0:
        print(f"El numero {i} es par") 
    else:
        print(f"El numero {i} es impar")