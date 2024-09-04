class Edadinvalida(Exception):
    pass    

def solicitar_Edad(mensaje):
    while True:
        try:
            edad = float(input(mensaje)) 
            return edad 
        except ValueError:
            print('Error: Ingresa un valor valido') 
           
def calcular_edad(edad):
    try:
        if edad < 18:
            raise ValueError('Eres menor de edad') 
        else:
            edad >= 18
            return 'Eres Adulto'  
    except ValueError as e:
        print(f'Error: {e}')   
       
# main
edad1 = solicitar_Edad('Ingresa tu edad: ')     
resultado = calcular_edad(edad1)   
print(resultado)