#listas(list)
frutas = ["tunas","guanabana","maraucuya"]#creacion de listas
numerosPrimos = [3,5,7,11]#creacion de listas
print(type(frutas))#el type nos indica que tipo de objeto es 'frutas'(en este caso es una lista)
print(type(numerosPrimos))# aca es lo mismo pregunta que tipo de objeto es 'numerosPrimos'(en este caso es una lista)
print(frutas[1])# aca estamos imprimiendo la pocicion 1 de la lista frutas
print(numerosPrimos[1])# aca estamos imprimiendo la pocicion 1 de la lista numerosPrimos
frutas[2] = "Naranjas" # aca estamos cambiando la string que esta en la pocicion 1 por esta nueva cadena llamada Naranja
print(frutas)
frutas.append("pera")# el .append es para agregar un nuevo elemento a mi lista que ira al final de la lista 
print(frutas)

#tuplas (las tuplas van entre parentesis) las tuplas no se pueden modificar
dimensiones = (1223, 3454)
coordenadas = (45, 65)
print(type(dimensiones))
print(type(coordenadas))

#conjuntos en los conjuntos no se repiten los elementos
colores={"rojo","verde","blanco"}
numeros_unicos = {1,2,3,4,5,6}

numeros_unicos.add(7)#agrega un elemento al conjunto
colores.remove("blanco")#elimina el elemento 
print(numeros_unicos)
print(colores)

print(len(numeros_unicos)) #el len me manda la cantidad de elementos que tiene el conjunto o lista o de cualquier estructura

#diccionarios (los diccionarios van entre llaves {})
personas={"nombre":"ana","edad":30,"ciudad":"tlaxcala"}
precios={"manzanas":12, "banana":23, "peras":3.5}
print(personas["nombre"])
print(precios["peras"])

#cambiar datos den los diccionarios
personas["edad"]= 31
print(personas)

#agregar nuevos elementos al diccionario
personas["ocupacion"]="Programador"
print(personas)


################################################### desafio################
# Desafío: Crear un diccionario

# Vas a crear un programa para obter informacion de un contacto. El programa debe:

# Obtener información del contacto desde la consola.
# Almacenar la información en un diccionario.
# Realizar algunas operaciones básicas con los datos almacenados.
# Imprimir los resultados.
# Requisitos:

# Obtener Datos de Consola:

# Usa input() para obtener el nombre,  el correo electrónico y el número de teléfono del contacto.
# Almacenar Datos:

# Almacena la información en un diccionario.
# Operaciones Básicas:

# Calcula el número total de caracteres en el nombre del contacto.
# Imprime la información completa del contacto.

nombre_contacto = input("Ingresa tu nombre: ")
email_contacto = input("Ingresa tu email: ")
numero_telelfono = int(input("Ingresa tu numero telefono: "))

diccionario_contacto = {"nombre":nombre_contacto, "email":email_contacto, "numero_telefono":numero_telelfono} #en este caso para agregar las variables no es necesario poner ni COMA ni un MAS
print(diccionario_contacto)
print(len(nombre_contacto))