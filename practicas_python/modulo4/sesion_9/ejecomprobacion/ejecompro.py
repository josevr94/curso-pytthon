
archivo = 'informacion.dat'

def escribe_archivo_inicial(archivo):
    with open(archivo,'w') as file:
        for i in range(1,6):
            file.write(f'Datos de informacion en la linea {i}\n')
    return print('Escrito')
             
def ejecomprobacion_9(archivo):
    
    with open(archivo,'a') as file:
        file.write('Hola Mundo\nEste en una nueva línea en el archivo\nagregando la segunda línea del archivo\nfinalizando la línea agregada')    
        
    return print('actualizado')    

# main

while True:
    try:
        respuesta = int(input('1.- crea el archivo con la informacion previa\n2.- escribe al final del archivo lo solicitado por el ejercicio\n3.-salir\nrespuesta: '))
        if respuesta == 1:
            escribe_archivo_inicial(archivo)
        if respuesta == 2:
            ejecomprobacion_9(archivo)   
        if respuesta == 3:
            break
    except ValueError:
        print('ingrese un valor valido')        