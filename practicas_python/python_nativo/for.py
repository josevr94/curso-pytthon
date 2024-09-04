# recorriendo una lista 
frutas=["Pera", "manzana", "sandia", "platano"]
for fruta in frutas:
    print(f"el nombre de la fruta es: {fruta}")
    
    # recorriendo una palabra
palabra= "python"  
for letra in palabra:
    print(f"La letra es: {letra.upper()}")
    
#  recorriendo diccionarios   
estudiantes={"matias": 10, "roberto": 7, "alex": 8} 
for nombre, nota in estudiantes.items():  #la funcion .items() sirver cuandi queremos trabajar con un diccionario que tiene string y numeros, items() separa estas cosas y me deja trabajar con dos elementos dentro del mismo ciclo 
    print(f"El nombre del estudiante es: {nombre}, y su calificacion es: {nota}")
    
# recorriendo numeros
numeros = [23,76,34,89,98,100]    
suma = 0
for numero in numeros:
    suma += numero
print(f"la suma de los numero es: {suma}")   
media = suma / len(numeros) 
print(f"la media de los numero es: {media}")

# sumar valores de un diccionario
ventas = {"enero":100, "febrrero":2000 ,"marzo":3000}
total_ventas =0
for mes, cantidad in ventas.items():
    total_ventas += cantidad
print(f"el total de las ventes es de {total_ventas}")

# for y if para recorrer listas     
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]   
numero_pares=[] 
for number in numbers:
    if number % 2 == 0:
        numero_pares.append(number)
print(f"los numeros pares son: {numero_pares}")        

# usando break
nums = [10,20,30,40,50,60,-5]
for num in nums:
    if num <= 0:
        print(f"el numero {num} no es positivo")
        break
else:
    print("todos los numeros son positivos")
    
    
######################################################################3

import random
numero_secreto = random.randint(1, 100)       

numero = int(input("hola intenta adivinar el numero secreto: "))
intentos = 10
for intento in range(intentos):
    if numero < numero_secreto:
        print(f"el numero {numero} es menor al numero secreto")
        intentos -= 1
        print(f"te quedan {intentos} intentos")
        numero = int(input("intentalo de nuevo: "))
    elif numero > numero_secreto:
        print(f"el numero {numero} es mayor al numero secreto")
        intentos -= 1
        print(f"te quedan {intentos} intentos")
        numero = int(input("intentalo de nuevo: "))
    else:
        numero == numero_secreto
        print(f"Felicidades, has adivinado el numero secreto y te quedaron  {intentos}")
        break
        


    