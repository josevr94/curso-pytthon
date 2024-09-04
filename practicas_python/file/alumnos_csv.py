import csv
#escribe un metodo para escribir en un archivo csv y poder usarlo despues
def escribir_csv(filename,datos):
    with open(filename,mode='w',newline="") as file:
        escritor_csv = csv.writer(file)
        escritor_csv.writerow(['Nombre','Apellido','Ciudad'])#cabecera de la tabla
        for fila in datos: #el ciclo es par que no se escriba todo pegado
            escritor_csv.writerow(fila)#datos que agregaremos despues
        print('Archivo creado con exito')
#metodo para leer un archivo csv y poder usarlo despues
def leer_csv(filename):   
    with open(filename,mode='r',newline="") as file:
        lector_csv = csv.reader(file)
        print("--------Mostrando datos---------")    
        for fila in lector_csv:            
            print(fila)
        
#metodo para agregar una archivo csv a otro csv
def agregar_csv(filename, registro):            
    with open(filename, mode='a',newline="") as file:
        escritor_csv = csv.writer(file)
        escritor_csv.writerow(registro)
        
datos_iniciales = [['belen','navarrete','santiago'],['belen2','navarrete','santiago'],['belen3','navarrete','santiago']] 
nombre_archivo = "file/csv/studiantes.csv"  
registro1 = ['jose','vinuela','paine']
registro12 = ['jose2','vinuela222','paine22']
escribir_csv(nombre_archivo,datos_iniciales)  
agregar_csv(nombre_archivo,registro1)  
agregar_csv(nombre_archivo,registro12)  
leer_csv(nombre_archivo)