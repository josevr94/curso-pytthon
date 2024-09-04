number = int(input("Ingresa un numero: "))

if number < 0:
    print("El numero ingresado es negativo.")
    if number % 2 == 0:
        print("El numero es par.")
    else:
        print("El numero es impar.")
else:
    print("El numero ingresado es positivo.")
    if number % 2 == 0:
        print("El numero es par.")
    else:
        print("El numero es impar.")