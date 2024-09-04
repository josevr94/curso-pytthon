posicion = 0
for i in "paralelepipedo":
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        posicion += 2 
        continue
    print(f"{posicion}.- {i}")    