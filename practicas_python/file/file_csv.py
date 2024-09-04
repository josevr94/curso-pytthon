import csv
#lectura de archivos con csv (excel)
with open('file/csv/nombres_y_edad.csv', 'r') as f:
    lector = csv.reader(f)
    for fila in lector:
        print(fila)

#escribir en un archivo csv
dato = [['Nombre','Edad'],['Edgard',34],['Gonzalo',33]]
with open('file/csv/nuevos_datos.csv', 'w', newline="") as f:  
    escribir = csv.writer(f)  
    for fila in dato:   
        escribir.writerow(fila)