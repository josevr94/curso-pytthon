# crear una funcion que calcule el area de un triangulo 
# tambien tiene que validar que los numero sean positivos

def area_rectangulo(a, b):
    if a < 0 or b < 0:
        return print("Ingresó un valor negatico, los valores deben ser positivos")
    else:
        return print("El area del rectangulo es: ",(a * b))
    
    
a = float(input("Ingresa la altura del rectangulo: "))
b = float(input("Ingresa la base del rectangulo: "))

area_rectangulo(a,b) 