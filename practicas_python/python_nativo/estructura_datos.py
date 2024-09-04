#lista(list)
frutas=["Tunas","Guanabana","Marucuya"]
numeroPrimos=[3,5,7,11]
print(type(frutas))
print(type(numeroPrimos))
print(frutas[0])
print(numeroPrimos[2])

frutas[0]="Mango"
print(frutas)

frutas.append("Lichi")
print(frutas)

numeroPrimos.append(13)
print(numeroPrimos)

#tupla
dimensiones = (1920,1080)
coordenadas = (10,20)
print(type(dimensiones))
print(type(coordenadas))
puntos=(10,20)
# puntos[1]=30 # no se puede asignar a tupla un nuevo valor

#conjunto 
colores={"rojo","verde","blanco","rojo"}
numeros_unicos= {1,2,3,4,5,1}
print(type(colores))
print(colores)
print(numeros_unicos)
numeros_unicos.add(6) #metodo para agrega al cojunt
print(numeros_unicos)
colores.remove("blanco") #metodo remover un elemento al cojunto
print(colores)
print(len(numeros_unicos))
print(len(colores))
#Diccionarios(dict)
personas={"nombre":"Ana","edad":30,"ciudad":"Tlaxcala"}
precios = {"manzana":12, "banana":5 , "cerezas":2.5}
print(type(personas))
print(type(precios))
print(personas["nombre"])
print(precios["manzana"])
 
personas["edad"]=31 #modificando un valor
print(personas)
personas["ocupacion"]="Programador"
print(personas)




