#operador and 
a = 10 
b = 20
resultado = (a>5) and (b<30)
print (resultado) #regresara true porque cumple en los dos casos, esto definido por el and 

#operador or
r = 5
x = 15
resultado2 = (r>10) or (x<20)
print (resultado2) #regresa true porque cumple en uno de los dos casos (el or es un O)

#operador not
#el operador not es el opuesto 
edad = 19
resultado3 = not(edad >=18)# en este caso diria 19 es mayor o igual a 18, eso es verdadero, pero como tiene el not, seria lo opuesto, por ende el resulta oseria false
print (resultado3) 

#operaciones usando diferentes opreadores
w=5
v=15
t=25
resultado4 = (w<10) and (v<20) or (t>20)
print(resultado4)

################# desafio ####################
# Desafío: Evaluación de Información Personal
# Descripción:

# Vas a crear un programa que obtiene información personal de tres personas desde la consola 
# y realiza algunos cálculos utilizando esta información. El programa debe:

# Obtener los nombres, edades y alturas de tres personas desde la consola.
# Calcular el promedio de las edades y alturas(flotante).
# Calcular el total de caracteres en los nombres.
# Imprimir los resultados.
# Requisitos:

# Obtener Datos de Consola:

# Usa la función input() para obtener el nombre, edad y altura de tres personas.
# Calcular Promedios y Totales:

# Calcula el promedio de las edades.
# Calcula el promedio de las alturas.
# Calcula el total de caracteres en los nombres.
# Mostrar Resultados:

# Imprime el promedio de las edades y alturas.
# Imprime el total de caracteres en los nombres.


nombre1 = input("ingresa tu nombre: ")
edad1 = int(input("ingresa tu edad:  "))
altura1 = float(input("ingresa tu altura: "))

nombre2 = input("ingresa tu nombre: ")
edad2 = int(input("ingresa tu edad: "))
altura2 = float(input("ingresa tu altura: "))

nombre3 = input("ingresa tu nombre: ")
edad3 = int(input("ingresa tu edad: "))
altura3 = float(input("ingresa tu altura: "))

promedioedad = (edad1 + edad2 + edad3)//3
promedioaltura = (altura1 + altura2 + altura3)//3
caracteresnombres1 = len(nombre1)
caracteresnombres2 = len(nombre2)
caracteresnombres3 = len(nombre3)
sumacaracteres= caracteresnombres1 + caracteresnombres2 + caracteresnombres3

print("El promedio de edades es: ", promedioedad)
print("El promedio de las alturas es de: ", promedioaltura)
print("La suma de los caracteres de los nombres es de: ", sumacaracteres)

