def solicitar_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Error: ingrese un número válido.")
def realizar_operacion(a, b, operador):
    try:
        if operador == "+":
            return a + b
        elif operador == "-":
            return a - b
        elif operador == "*":
            return a * b
        elif operador == "/":
            if b == 0:
                raise ZeroDivisionError("Error no se puede dividir por cero")               
            return a / b
        else:
            raise ValueError("Operacion no Valida")
    
    except ValueError as e:
        print(e) 
        return None                             
#main
num1 = solicitar_numero("Introduce el primero numer: ")
num2 = solicitar_numero("Introduce el segundo numero: ")

operacion = input("Introduce el operador: ")

resultado = realizar_operacion(num1, num2, operacion)
print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")