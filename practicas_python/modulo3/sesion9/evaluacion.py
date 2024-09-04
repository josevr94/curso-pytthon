# crear funciones que sumen, resten, multipiquen, dividan

def suma(a,b):
    return a + b
def resta(a,b):
    return a - b
def multiplicacion(a,b):
    return a * b
def dividir(a,b):
    if b == 0:
        return "Error, no se puede dividir entre 0"
    else:
        return a / b
def tuplas(a,b):
    diccionario = {
        "Suma": suma(a,b),
        "Resta": resta(a,b),
        "Multiplicacion": multiplicacion(a,b),
        "Division": dividir(a,b) 
    }
    
    return print(diccionario)    



a = float(input("Ingresa el primer valor: "))
b = float(input("Ingresa el segundo valor: "))
tuplas(a,b)