lista_de_listas = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
diccionario = {}
claves = ["A", "B", "C", "D"]
for i, lista in enumerate(lista_de_listas):
    if lista[0] == 0:
        continue
    else:    
        diccionario[claves[i]]= lista
        
    for numero in lista:
        if numero == 0:
            continue
        else:
            print(numero)   
print(diccionario) 