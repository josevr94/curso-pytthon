archivo = 'informacion.dat'

def creando_archivo(archivo):
    with open(archivo,'a') as file:
        for i in range(1,6):
            file.write(f'Datos de informacion en la linea {i}\n')
        print('Escrito') 
    with open(archivo,'a') as file:
        file.write('Hola Mundo\nEste en una nueva línea en el archivo\nagregando la segunda línea del archivo\nfinalizando la línea agregada')    
    return print('archivo creado')
        
def cambiando_palabra(archivo):
    
    contador = 0
    with open(archivo,'r') as file:
        contenido = file.readlines()
        
    with open(archivo, 'r') as info:
        contenido2 = info.read()
                
    with open(archivo,'w') as f:
        for linea in contenido:
            palabra_guardada = linea.count('informacion')
            contador += palabra_guardada
        modificado = contenido2.replace('informacion','Procesamiento')    
        f.write(modificado)    
    return print(f'Se realizaron {contador} remplazos')    
    
        
# main
while True:
    
    try:
        respuesta = int(input('1.-Crea archivo para realizar la evaluacion\n2.-Realiza el ejercicio requerido evaluacion sesion 9\n3.-Salir\nIngresa respuesta: '))
        if respuesta == 1:
            creando_archivo(archivo)
        if respuesta == 2:
            cambiando_palabra(archivo)
        if respuesta == 3:
            break        
    except ValueError:
        print('respuesta invalida')        
        
       