#copiar el contenido de un archivo a otro
def copiar_archivo(archivo_origen, archivo_destino):
    try:
        #abrimo el archivo origen en modo lectura por la 'r'
        with open(archivo_origen, "r") as origen:
            contenido =origen.read()
        #abrir el archivo destino en modo escritura con la 'w'
        with open(archivo_destino, 'w') as destino:
            destino.write(contenido) #escribe el contenido en el nuevo archivo
    except FileNotFoundError:
        print(f"El archivo {archivo_origen} no existe")
# contar palabras de un archivo 
def contar_palabras(archivo):
    try:
        with open(archivo, 'r') as f:
            contenido = f.read() #leemos todo el contenido y lo guardamos en la variable contenido
            palabras = contenido.split()
            print(f'el archivo {archivo} contiene {len(palabras)} palabras')    
    except FileNotFoundError:
        print(f"El archivo: {archivo} no existe")       
#remplazar palabras en un archivo
def remplazar_palabra(archivo_origen,palabra_buscar,palabra_remplazo,archivo_destino):
    try:
        with open(archivo_origen, 'r') as origen:
            contenido = origen.read()
        #remplazar la palabra
        contenido_modificado = contenido.replace(palabra_buscar,palabra_remplazo)
        # guarda el contenido modificado en un archivo nuevo 
        with open(archivo_destino, 'w') as destino:
            destino.write(contenido_modificado)           
    
    except FileNotFoundError:
        print(f"El archivo: {archivo_origen} no existe")            
#main
copiar_archivo("file/ejemplo.txt","file/ejemplo2.txt")        
contar_palabras('file/ejemplo2.txt')        
remplazar_palabra('file/ejemplo2.txt','jose','jose luis','file/ejemplo3.txt')