# metodos
def suma(a,b):
    return a + b
def resta (a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    return a/b
def solicitar_numeros():
    num1 = float(input("ingresa el primero numero: "))
    num2 = float(input("ingresa el segundo numero: "))
    return num1, num2
def mostrar_resultado(num1,num2,resultado):
    print(f"el resultado de la suma de los numero {num1} y {num2} es {resultado}")
    

def calculadora():
    print("-------------Bienvenido a la Calculadora 0077------------------")
    while True:
        print("\nSelecciona una operacion")
        print("1.-Sumar")
        print("2.-Restar")
        print("3.-multiplicar")
        print("4.-Dividir")
        print("5.-Salir")
        opcion = int(input("ingresa tu opcion del 1 al 5: "))
        
        if opcion ==1:
            num1,num2= solicitar_numeros()
            resultado = suma(num1,num2)
            mostrar_resultado(num1,num2,resultado)
        elif opcion == 2:
            num1,num2= solicitar_numeros()
            resultado = resta(num1,num2)
            mostrar_resultado(num1,num2,resultado)
        elif opcion == 3:
            num1,num2= solicitar_numeros()
            resultado = multiplicar(num1,num2)
            mostrar_resultado(num1,num2,resultado)
        elif opcion == 4:
            num1,num2= solicitar_numeros()
            if num2 == 0:
                print("Error, no se puede dividir entre 0")
            else:
                resultado = dividir(num1,num2)
                mostrar_resultado(num1,num2,resultado)
        elif opcion == 5:
            print("Gracias por usar la calculadora 0077")
            break
        else:
            print("Opcion invalida, intentalo de nuevo")
                    
calculadora()                    