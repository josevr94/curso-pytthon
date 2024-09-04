# Desafío: Adivina el Número Secreto
# Objetivo: Implementar un juego en Python donde el usuario debe adivinar un número secreto entre 1 y 100. 
# El programa debe indicar si el número ingresado es mayor o menor al número secreto y continuar preguntando hasta que el usuario lo adivine.

# Instrucciones:
# Generar un número secreto aleatorio entre 1 y 100.
# Pedir al usuario que adivine el número secreto.
# Comparar el número ingresado por el usuario con el número secreto:
# Si el número ingresado es mayor que el número secreto, mostrar el mensaje: "El número secreto es menor. Intenta de nuevo."
# Si el número ingresado es menor que el número secreto, mostrar el mensaje: "El número secreto es mayor. Intenta de nuevo."
# Si el número ingresado es igual al número secreto, mostrar el mensaje: "¡Felicidades! Has adivinado el número secreto." y terminar el juego.
# Continuar pidiendo al usuario que adivine hasta que acierte el número secreto.
import random
numero_secreto = random.randint(1, 100)
numero = int(input("hola intenta adivinar el numero secreto: "))
while numero != numero_secreto:
    if numero < numero_secreto:
        print(f"el numero {numero} es menor al Numero secreto")
        numero = int(input("intentalo de nuevo: "))
        
    elif numero > numero_secreto:
        print(f"el numero {numero} es mayor al Numero secreto")
        numero = int(input("intentalo de nuevo: "))
        
else:
    print("Felicidades, has adivinado el numero secreto!") 
    print(f"El numero secreto era {numero}")       