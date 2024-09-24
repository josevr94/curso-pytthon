def leer_escribir():
    archivo = 'informacion.dat'
    try:
        with open(archivo,'a') as crear:
            crear.write('')
        with open(archivo,'r') as f:
            contenido = f.read()
            if contenido == '':
                with open(archivo,'a') as file:
                    for i in range(1,6):
                        file.write(f'Datos de informacion en la linea {i}\n')
                    print('Escrito')                     
            else:                
                print(f'El archivo informacion.dat ya existe, ha sido creado previamente\n{contenido}')            
    except FileNotFoundError:
        print('no se encontro el archivo')          
            
# main            
leer_escribir()     