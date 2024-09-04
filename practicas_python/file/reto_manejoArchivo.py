def abrir_archivo(archivo):
    try:        
        with open(archivo, 'r') as f:           
            contenido = f.read()
        
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encuentra.")
        
    return contenido 
def escritura_archivo(archivo, contenido):
    try:
        with open(archivo, 'a') as f:
            f.write(contenido + '\n')       
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encuentra.")        
      
def contar_lineas( archivo):           
    with open(archivo, 'r') as archivo:
        tareas = archivo.readlines()
    print(f"Número total de tareas: {len(tareas)}")
    return len(tareas)   
def agregar_tareas(archivo):
    while True:
        tarea = input("Ingresa tus tareas aquí:.....(escribre 'salir' para terminar)") 
        try:
            if tarea == 'salir':
                break
            # with open(archivo, 'a') as f:
            #     f.write('\n'+tarea)
                
            contenido = escritura_archivo(archivo,tarea)    
            # contenido.write(tarea)        
            print('Tarea agregada')
        except ValueError as e:
            print(f'Error: {e}')                
def copia_contenido(archivo_origen,archivo_nuevo):
    try:
        #revisar esta parte
        contenido1 = abrir_archivo(archivo_origen)
        destino = escritura_archivo(archivo_nuevo)
    except FileNotFoundError:
        print(f"El archivo {archivo_origen} no se encuentra.")
    return destino
def conta_palabras(archivo):
    try:
        with open(archivo, 'r') as archivo:
            contenido = archivo.read()
            palabra = contenido.split()                   
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encuentra.")   
    
    return print(f"El numero de palabras del archivo {archivo} es de: {len(palabra)}")  

def reemplazar_palabra(archivo,archivo_destino):
    palabraA_buscar = input("Ingresa la palabra que quieres reemplazar: ")
    palabraPara_remplazar = input("Ingresa lo que quieras agregar: ")
    try:
        abrir_archivo(archivo)
        contenido = abrir_archivo.read() 
        nuevo_contenido = contenido.replace(palabraA_buscar, palabraPara_remplazar)   
        # abrir_archivoEscritura(archivo_destino)
        archivo.write(nuevo_contenido)
        
    except FileExistsError:
        print(f"Escribe la palabra que deseas reemplazar:")                  
        
        
        
# main
nombre_archivo = "file/ejemplos_textos/ejemplo2.txt"
# contenido.abrir_archivo(nombre_archivo) 
agregar_tareas(nombre_archivo) 
