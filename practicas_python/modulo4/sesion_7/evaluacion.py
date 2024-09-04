class RangosSalarioError(Exception):
    pass    

def salario(mensaje):
    sueldo = float(input(mensaje))
    try:
        if 1000 >= sueldo <= 2000:
            raise RangosSalarioError(f'Salario no es definido en el rango 1000 a 2000)')
        return print('tu sueldo esta en el rango')
        
            
    except RangosSalarioError as e:
        print(f'Error: {e}') 
        
# main

salario('Ingresa tu salario: ')        
